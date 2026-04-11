#!/usr/bin/env python3
"""Coleta de documentos da legislacao da PROGRAD em modo seguro.

Regras principais:
- coleta links PDF e boletimoficial;
- nao apaga arquivos locais;
- nao sobrescreve arquivo existente com hash divergente;
- gera manifest e relatorios para revisao humana.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import ssl
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Iterable


BASE_URL = "https://prograd.ufms.br/legislacao/"
USER_AGENT = "coleta-legislacao-prograd/1.0 (+docs sync)"
INSECURE_TLS_HOSTS = {"preg.bellatrix.ufms.br"}
ASSETS_DIRNAME = "assets"

SUBFOLDER_MAP = [
    (
        "https://prograd.ufms.br/legislacao/legislacao-avaliacao/",
        "legislacao-avaliacao",
    ),
    (
        "https://prograd.ufms.br/legislacao/legislacao-educacional-nacional/",
        "legislacao-educacional-nacional",
    ),
    ("https://prograd.ufms.br/legislacao/legislacao-estagio/", "legislacao-estagio"),
    (
        "https://prograd.ufms.br/legislacao/legislacao-formacao-de-professores/",
        "legislacao-formacao-de-professores",
    ),
    (
        "https://prograd.ufms.br/legislacao/legislacao-geral-da-ufms/",
        "legislacao-geral-da-ufms",
    ),
    (
        "https://prograd.ufms.br/legislacao/legislacao-geral-graduacao/",
        "legislacao-geral-graduacao",
    ),
    ("https://prograd.ufms.br/legislacao/legislacao-ingresso/", "legislacao-ingresso"),
    (
        "https://prograd.ufms.br/legislacao/legislacao-professor-substituto/",
        "legislacao-professor-substituto",
    ),
    ("https://prograd.ufms.br/legislacao/normas/", "normas"),
    (
        "https://prograd.ufms.br/regulamentos-de-ccnd-da-graduacao/",
        "regulamentos-de-ccnd-da-graduacao",
    ),
    (
        "https://prograd.ufms.br/legislacao/regulamentos-de-ccnd-da-graduacao/",
        "regulamentos-de-ccnd-da-graduacao",
    ),
    (
        "https://prograd.ufms.br/programas/programa-de-estudantes-convenio-de-graduacao-pec-g/",
        "programas/programa-de-estudantes-convenio-de-graduacao-pec-g",
    ),
    (
        "https://prograd.ufms.br/a-prograd/digac/programa-de-estudantes-convenio-de-graduacao-pec-g/",
        "programas/programa-de-estudantes-convenio-de-graduacao-pec-g",
    ),
    (
        "https://prograd.ufms.br/legislacao/legislacao-programa-de-educacao-tutorial/",
        "programas",
    ),
    (
        "https://prograd.ufms.br/programas-e-projetos/programa-de-educacao-tutorial-pet/",
        "programas",
    ),
    ("https://prograd.ufms.br/legislacao/legislacao-monitoria/", "programas"),
    (
        "https://prograd.ufms.br/programas-e-projetos/projeto-de-ensino-de-graduacao/",
        "programas",
    ),
]

KEYWORD_SUBFOLDER_MAP = [
    ("pec-g", "programas/programa-de-estudantes-convenio-de-graduacao-pec-g"),
    (
        "programa-de-estudantes-convenio-de-graduacao",
        "programas/programa-de-estudantes-convenio-de-graduacao-pec-g",
    ),
    ("regulamento-dos-cursos-de-graduacao", "legislacao-geral-graduacao"),
    ("resolucao-cograd-n-430", "legislacao-geral-graduacao"),
    ("monitoria", "programas"),
    ("educacao-tutorial", "programas"),
    ("pet", "programas"),
    ("projeto-de-ensino-de-graduacao", "programas"),
    ("peg", "programas"),
]

HTML_HREF_RE = re.compile(r"href\s*=\s*(['\"])(.*?)\1", re.IGNORECASE)
A_TAG_RE = re.compile(
    r"<a\b[^>]*?href\s*=\s*(['\"])(.*?)\1[^>]*>(.*?)</a>",
    re.IGNORECASE | re.DOTALL,
)
HTML_TAG_RE = re.compile(r"<[^>]+>")
PDF_IN_TEXT_RE = re.compile(
    r"https?://[^\s\"'<>]+\.pdf(?:\?[^\s\"'<>]*)?", re.IGNORECASE
)


@dataclass(frozen=True)
class Candidate:
    document_url: str
    source_page: str
    link_text: str | None = None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    clean_path = parsed.path or "/"
    if clean_path != "/" and clean_path.endswith("/"):
        clean_path = clean_path[:-1]
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), clean_path, parsed.query, "")
    )


def safe_filename(name: str) -> str:
    name = name.strip().replace("\x00", "")
    if not name:
        return "documento.pdf"
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    if len(name) > 180:
        stem, ext = os.path.splitext(name)
        name = stem[:170] + ext
    return name


def clean_anchor_text(text: str) -> str:
    text = HTML_TAG_RE.sub(" ", text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text).strip(" -\t\r\n")
    return text


def encode_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parsed.path, safe="/%-._~")
    query_pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = urllib.parse.urlencode(query_pairs, doseq=True)
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, path, query, parsed.fragment)
    )


def is_supported_doc_link(url: str) -> bool:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if path.endswith(".pdf"):
        return True
    if host == "boletimoficial.ufms.br":
        return True
    return False


def is_allowed_page(url: str) -> bool:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    host = parsed.netloc.lower()
    path = parsed.path
    if host != "prograd.ufms.br":
        return False
    return (
        path.startswith("/legislacao/")
        or path.startswith("/programas/")
        or path.startswith("/regulamentos-de-ccnd-da-graduacao/")
    )


def fetch_url(url: str, timeout: int) -> tuple[bytes, str, str]:
    encoded_url = encode_url(url)
    req = urllib.request.Request(encoded_url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").lower()
            final_url = resp.geturl()
        return data, ctype, final_url
    except urllib.error.URLError as exc:
        host = urllib.parse.urlsplit(encoded_url).netloc.lower()
        if host not in INSECURE_TLS_HOSTS or "CERTIFICATE_VERIFY_FAILED" not in str(
            exc
        ):
            raise

    insecure_context = ssl._create_unverified_context()
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=insecure_context)
    )
    with opener.open(req, timeout=timeout) as resp:
        data = resp.read()
        ctype = (resp.headers.get("Content-Type") or "").lower()
        final_url = resp.geturl()
    return data, ctype, final_url


def extract_links(base_url: str, html_text: str) -> list[tuple[str, str | None]]:
    links: list[tuple[str, str | None]] = []

    for _, raw_href, raw_text in A_TAG_RE.findall(html_text):
        candidate = unescape(raw_href.strip())
        if not candidate or candidate.startswith("#"):
            continue
        full = urllib.parse.urljoin(base_url, candidate)
        label = clean_anchor_text(raw_text)
        links.append((full, label if label else None))

    for _, raw in HTML_HREF_RE.findall(html_text):
        candidate = unescape(raw.strip())
        if not candidate or candidate.startswith("#"):
            continue
        full = urllib.parse.urljoin(base_url, candidate)
        links.append((full, None))

    for raw in PDF_IN_TEXT_RE.findall(html_text):
        links.append((raw, None))

    deduped: dict[str, tuple[str, str | None]] = {}
    for item_url, item_text in links:
        norm = normalize_url(item_url)
        if norm not in deduped:
            deduped[norm] = (item_url, item_text)
            continue
        if deduped[norm][1] is None and item_text:
            deduped[norm] = (item_url, item_text)
    return list(deduped.values())


def resolve_subfolder(source_page: str, document_url: str) -> str | None:
    source_norm = normalize_url(source_page)
    doc_norm = normalize_url(document_url)
    for prefix, subfolder in SUBFOLDER_MAP:
        pref_norm = normalize_url(prefix)
        if source_norm.startswith(pref_norm) or doc_norm.startswith(pref_norm):
            return subfolder

    source_joined = (source_page + " " + document_url).lower()
    for keyword, subfolder in KEYWORD_SUBFOLDER_MAP:
        if keyword in source_joined:
            return subfolder

    return None


def filename_from_candidate(_candidate: Candidate, final_url: str) -> str:
    parsed = urllib.parse.urlsplit(final_url)
    host = parsed.netloc.lower()

    if host == "boletimoficial.ufms.br":
        q = urllib.parse.parse_qs(parsed.query)
        doc_id = (q.get("id") or ["sem-id"])[0]
        return safe_filename(f"BOLETIMOFICIAL-id-{doc_id}.pdf")

    base = urllib.parse.unquote(os.path.basename(parsed.path))
    return safe_filename(base)


def previous_local_path(previous: dict | None, storage_root: Path) -> Path | None:
    if not previous:
        return None
    local_path = previous.get("local_path")
    if not local_path:
        return None
    candidate = (Path.cwd() / local_path).resolve()
    try:
        candidate.relative_to(storage_root)
    except ValueError:
        return None
    return candidate


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"entries": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"entries": []}


def crawl(
    base_url: str, max_pages: int, timeout: int
) -> tuple[list[Candidate], list[dict], list[str]]:
    queue: deque[str] = deque([base_url])
    visited: set[str] = set()
    found: dict[str, Candidate] = {}
    crawl_errors: list[dict] = []
    analyzed_pages: list[str] = []

    while queue and len(visited) < max_pages:
        current = queue.popleft()
        current_norm = normalize_url(current)
        if current_norm in visited:
            continue
        visited.add(current_norm)

        try:
            body, ctype, final_url = fetch_url(current, timeout=timeout)
        except urllib.error.URLError as exc:
            crawl_errors.append({"url": current, "error": str(exc)})
            continue
        except TimeoutError as exc:
            crawl_errors.append({"url": current, "error": str(exc)})
            continue

        if "text/html" not in ctype and "application/xhtml+xml" not in ctype:
            continue

        text = body.decode("utf-8", errors="replace")
        analyzed_pages.append(final_url)
        for link, link_text in extract_links(final_url, text):
            if is_supported_doc_link(link):
                doc_norm = normalize_url(link)
                if doc_norm not in found:
                    found[doc_norm] = Candidate(
                        document_url=link, source_page=final_url, link_text=link_text
                    )
                continue

            if is_allowed_page(link):
                link_norm = normalize_url(link)
                if link_norm not in visited:
                    queue.append(link)

    return list(found.values()), crawl_errors, analyzed_pages


def download_candidates(
    candidates: Iterable[Candidate],
    output_dir: Path,
    timeout: int,
    previous_manifest: dict,
) -> tuple[list[dict], list[dict], list[dict], list[dict], list[dict]]:
    storage_root = output_dir / ASSETS_DIRNAME
    previous_by_url = {
        item.get("source_url"): item
        for item in previous_manifest.get("entries", [])
        if item.get("source_url")
    }

    new_files: list[dict] = []
    unchanged: list[dict] = []
    changed_pending: list[dict] = []
    failures: list[dict] = []
    entries: list[dict] = []

    for candidate in candidates:
        source_url = candidate.document_url
        previous = previous_by_url.get(source_url)
        folder_rel = resolve_subfolder(candidate.source_page, source_url)
        if folder_rel is None and previous_local_path(previous, storage_root) is None:
            failures.append(
                {
                    "source_url": source_url,
                    "source_page": candidate.source_page,
                    "error": "sem-mapeamento",
                }
            )
            continue

        try:
            payload, ctype, final_url = fetch_url(source_url, timeout=timeout)
        except Exception as exc:  # noqa: BLE001
            failures.append(
                {
                    "source_url": source_url,
                    "source_page": candidate.source_page,
                    "error": str(exc),
                }
            )
            continue

        if not payload.startswith(b"%PDF"):
            failures.append(
                {
                    "source_url": source_url,
                    "source_page": candidate.source_page,
                    "error": f"nao-e-pdf (content-type={ctype})",
                }
            )
            continue

        previous_path = previous_local_path(previous, storage_root)
        if previous_path is not None:
            destination = previous_path
            destination_dir = destination.parent
        else:
            filename = filename_from_candidate(candidate, final_url)
            destination_dir = storage_root / folder_rel
            destination = destination_dir / filename

        destination_dir.mkdir(parents=True, exist_ok=True)

        incoming_hash = sha256_bytes(payload)
        incoming_size = len(payload)

        rel_path = os.path.relpath(destination, Path.cwd())
        entry_base = {
            "source_url": source_url,
            "resolved_url": final_url,
            "source_page": candidate.source_page,
            "local_path": rel_path,
            "sha256": incoming_hash,
            "size_bytes": incoming_size,
            "updated_at": now_iso(),
            "status": "",
        }

        if not destination.exists():
            destination.write_bytes(payload)
            info = dict(entry_base)
            info["status"] = "new"
            new_files.append(info)
            entries.append(info)
            continue

        existing_hash = sha256_file(destination)
        if existing_hash == incoming_hash:
            info = dict(entry_base)
            info["status"] = "unchanged"
            unchanged.append(info)
            entries.append(info)
            continue

        existing_size = destination.stat().st_size
        doc_host = urllib.parse.urlsplit(final_url).netloc.lower()
        if doc_host == "boletimoficial.ufms.br" and existing_size == incoming_size:
            info = dict(entry_base)
            info["status"] = "unchanged-size-match"
            info["note"] = (
                "hash divergente com mesmo tamanho em boletimoficial; mantido como inalterado por seguranca"
            )
            unchanged.append(info)
            entries.append(info)
            continue

        suffix = datetime.now().strftime("%Y%m%d")
        pending_name = destination.stem + f".REVISAO-{suffix}" + destination.suffix
        pending_path = destination.with_name(pending_name)
        pending_path.write_bytes(payload)

        info = dict(entry_base)
        info["status"] = "changed-pending-review"
        info["existing_local_path"] = os.path.relpath(destination, Path.cwd())
        info["review_copy_path"] = os.path.relpath(pending_path, Path.cwd())
        if previous:
            info["previous_sha256"] = previous.get("sha256")
            info["previous_size_bytes"] = previous.get("size_bytes")
        changed_pending.append(info)
        entries.append(info)

    return new_files, unchanged, changed_pending, failures, entries


def render_markdown_report(report: dict) -> str:
    lines: list[str] = []
    lines.append("# Relatorio de coleta de legislacao (modo seguro)")
    lines.append("")
    lines.append(f"- data_hora_utc: {report['generated_at']}")
    lines.append(f"- base_url: `{report['base_url']}`")
    lines.append(f"- paginas_analisadas: {report['summary']['pages_analyzed']}")
    lines.append(
        f"- links_documento_identificados: {report['summary']['doc_links_found']}"
    )
    lines.append(f"- novos_arquivos: {report['summary']['new_files']}")
    lines.append(f"- inalterados: {report['summary']['unchanged']}")
    lines.append(
        f"- novas_versoes_pendentes: {report['summary']['changed_pending_review']}"
    )
    lines.append(f"- falhas: {report['summary']['failures']}")
    lines.append("")

    lines.append("## Novos arquivos")
    lines.append("")
    if report["new_files"]:
        for item in report["new_files"]:
            lines.append(f"- `{item['local_path']}` <= `{item['source_url']}`")
    else:
        lines.append("- Nenhum arquivo novo.")
    lines.append("")

    lines.append("## Novas versoes (revisao humana)")
    lines.append("")
    if report["changed_pending"]:
        for item in report["changed_pending"]:
            lines.append(f"- existente: `{item['existing_local_path']}`")
            lines.append(f"  - copia para revisao: `{item['review_copy_path']}`")
            lines.append(f"  - origem: `{item['source_url']}`")
    else:
        lines.append("- Nenhuma divergencia de hash detectada.")
    lines.append("")

    lines.append("## Falhas e pendencias")
    lines.append("")
    if report["failures"]:
        for item in report["failures"]:
            lines.append(
                f"- `{item.get('source_url', item.get('url', 'sem-url'))}`: {item['error']}"
            )
    else:
        lines.append("- Nenhuma falha.")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Coleta de legislacao da PROGRAD em modo seguro"
    )
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Diretorio raiz da coleta; arquivos irao para <output-dir>/assets",
    )
    parser.add_argument(
        "--state-file", default="assets/.coleta-legislacao-manifest.json"
    )
    parser.add_argument(
        "--report-json", default="assets/.coleta-legislacao-report.json"
    )
    parser.add_argument("--report-md", default="assets/.coleta-legislacao-report.md")
    parser.add_argument("--max-pages", type=int, default=80)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    state_file = Path(args.state_file).resolve()
    report_json = Path(args.report_json).resolve()
    report_md = Path(args.report_md).resolve()

    output_dir.mkdir(parents=True, exist_ok=True)
    state_file.parent.mkdir(parents=True, exist_ok=True)
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_md.parent.mkdir(parents=True, exist_ok=True)

    previous_manifest = load_manifest(state_file)
    candidates, crawl_errors, analyzed_pages = crawl(
        args.base_url, args.max_pages, args.timeout
    )

    new_files, unchanged, changed_pending, download_failures, entries = (
        download_candidates(
            candidates=candidates,
            output_dir=output_dir,
            timeout=args.timeout,
            previous_manifest=previous_manifest,
        )
    )

    failures = [*crawl_errors, *download_failures]

    manifest = {
        "generated_at": now_iso(),
        "base_url": args.base_url,
        "total_entries": len(entries),
        "entries": entries,
    }
    state_file.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    report = {
        "generated_at": now_iso(),
        "base_url": args.base_url,
        "summary": {
            "pages_analyzed": len(analyzed_pages),
            "doc_links_found": len(candidates),
            "new_files": len(new_files),
            "unchanged": len(unchanged),
            "changed_pending_review": len(changed_pending),
            "failures": len(failures),
        },
        "new_files": new_files,
        "unchanged": unchanged,
        "changed_pending": changed_pending,
        "failures": failures,
    }

    report_json.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    report_md.write_text(render_markdown_report(report), encoding="utf-8")

    print(json.dumps(report["summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
