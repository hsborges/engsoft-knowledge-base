---
name: coleta-legislacao-prograd
description: Coleta periodica, em modo seguro, de PDFs da legislacao da PROGRAD a partir de `https://prograd.ufms.br/legislacao/` e paginas relacionadas, salvando somente em `{root}/assets`. Use sempre que o usuario pedir para coletar, sincronizar, atualizar ou verificar novos documentos da legislacao de graduacao da UFMS.
---

Esta skill padroniza a coleta recorrente de documentos normativos da PROGRAD com foco exclusivo em download e organizacao dos arquivos em `{root}/assets`.

## Quando usar

Use esta skill quando o usuario pedir para:

- atualizar a base de legislacao da graduacao da UFMS;
- coletar novos documentos do portal da PROGRAD;
- verificar divergencias entre o site e o acervo local em `assets`;
- rodar sincronizacao periodica de PDFs e links do boletim oficial.

Use mesmo que o usuario nao diga a palavra "skill".

## Fontes autorizadas

- URL raiz: `https://prograd.ufms.br/legislacao/`.
- Paginas filhas no mesmo contexto de legislacao (inclusive `programas` e `regulamentos` quando referenciados na raiz).
- Tipos de documento aceitos:
- links que terminam em `.pdf`;
- links de `https://boletimoficial.ufms.br/...` que retornem PDF.

Nao usar outras origens sem pedido explicito do usuario.

Para links legados de `preg.bellatrix.ufms.br`, esta skill aplica fallback de TLS inseguro por padrao para contornar certificado antigo e reduzir perdas de coleta.

## Regra obrigatoria de seguranca (modo seguro)

Esta skill opera em modo seguro por padrao:

- nao apagar arquivos existentes em `{root}/assets`;
- salvar novos PDFs em `{root}/assets/...`;
- nao sobrescrever automaticamente um PDF existente quando o conteudo divergir;
- salvar nova versao com sufixo de revisao para validacao humana;
- sempre gerar relatorio tecnico da coleta.

## Fluxo de execucao

1. Rodar o script de coleta da skill:

```bash
python3 ".agents/skills/coleta-legislacao-prograd/scripts/collect_legislacao.py" \
  --output-dir "." \
  --state-file "assets/.coleta-legislacao-manifest.json" \
  --report-json "assets/.coleta-legislacao-report.json" \
  --report-md "assets/.coleta-legislacao-report.md"
```

- Conferir o relatorio Markdown gerado.
- Apresentar ao usuario:
  - arquivos novos baixados;
  - arquivos com nova versao detectada (pendente de decisao);
  - links com falha.

## Regra de nomeacao de arquivos

- Para novos downloads de links PDF diretos, manter o nome do proprio arquivo na URL final (basename do PDF).
- Para links do Boletim Oficial, usar como estrategia principal `BOLETIMOFICIAL-id-<id>.pdf`.
- Para URLs ja registradas no manifesto, manter o caminho local anterior (em `{root}/assets`) para evitar renomeacoes em lote a cada coleta.

## Mapeamento de destino

O mapeamento de pagina de origem para subpasta local segue `references/mapeamento-subpastas.md`.

Se um documento nao casar com mapeamento conhecido, registrar como pendencia no relatorio, sem mover/renomear arquivos existentes.

A skill tambem aplica fallback por palavras-chave do URL/pagina (ex.: `pec-g`, `resolucao-cograd-n-430`, `monitoria`, `pet`, `projeto-de-ensino-de-graduacao`) para reduzir `sem-mapeamento`.

## Saida obrigatoria ao usuario

Sempre entregar:

- Status da coleta:

- total de links analisados;
- quantos PDFs validos foram identificados;
- quantos arquivos novos foram baixados.

- Itens para revisao humana:

- novas versoes detectadas (sem sobrescrita);
- documentos sem mapeamento de pasta;
- links com erro.

- Arquivos de evidencias:

- `assets/.coleta-legislacao-manifest.json`
- `assets/.coleta-legislacao-report.json`
- `assets/.coleta-legislacao-report.md`

## Nao fazer

- Nao apagar documentos locais por ausencia na origem.
- Nao tratar HTML comum como documento final.
- Nao editar documentos fora de `assets`.
