---
name: ufms-docs
description: Diretrizes para consultas documentais no acervo `docs/`, com foco em rastreabilidade, precisao de fonte e resposta acionavel. Use sempre que houver duvida sobre regras, procedimentos, cursos, atos normativos, prazos, competencias, vigencia, alteracao/revogacao, ou quando a resposta depender de documentos internos da UFMS. Nao use `docs/faq/` como fonte primaria.
---

# UFMS Docs

Esta skill orienta consultas, interpretacao e respostas com base no acervo [`docs/`](../../../docs/), com exclusao explicita de [`docs/faq/`](../../../docs/faq/).

## When to Use This Skill

Use esta skill quando o usuario:

- pedir resposta baseada em documentos do repositorio `docs/`;
- perguntar sobre regras, prazos, competencias, procedimentos, fluxo academico ou documentos de curso;
- pedir interpretacao de atos normativos, regulamentos, PPCs ou documentos institucionais;
- precisar de resposta com citacao rastreavel de arquivo e, quando aplicavel, de dispositivo.

Nao use esta skill para opinioes sem base documental, nem para responder apenas por memoria quando houver fonte no acervo.

## Mandatory Source Scope Rule

Escopo permitido:

- incluir todo o acervo em [`docs/`](../../../docs/), exceto [`docs/faq/`](../../../docs/faq/).

Restricao obrigatoria:

- nao usar arquivos de `docs/faq/` como fonte de verdade para fundamentacao.
- se `docs/faq/` for citado pelo usuario, tratar apenas como material de apoio de linguagem, nunca como base normativa/documental primaria.

## Mandatory Input Rule

Siga obrigatoriamente esta ordem:

1. Identificar a pasta raiz mais aderente em `docs/` (ex.: `cursos/`, `legislacao/`), ignorando `faq/`.
2. Abrir o `README.md` da pasta raiz escolhida (ex.: [`docs/cursos/README.md`](../../../docs/cursos/README.md) ou [`docs/legislacao/README.md`](../../../docs/legislacao/README.md)).
3. Identificar subpasta(s) relevante(s) pelo indice.
4. Abrir o `README.md` da subpasta antes de ler PDFs/arquivos finais.
5. Carregar no contexto apenas arquivos potencialmente relevantes para a pergunta.

Excecao: se o usuario indicar expressamente um arquivo especifico, voce pode iniciar por ele; ainda assim, valide no `README.md` da pasta para confirmar contexto, vigencia (quando normativo) e possiveis documentos correlatos.

## Current Topic Map (docs/)

- [`cursos/`](../../../docs/cursos/README.md): documentos por curso (ex.: PPC, resolucoes internas de curso, tabelas e anexos).
- [`legislacao/`](../../../docs/legislacao/README.md): atos normativos institucionais e nacionais relacionados ao contexto academico.

## Consultation Workflow

1. Classificar a pergunta (tema principal + tema(s) secundario(s)).
2. Escolher a trilha de consulta (`cursos` ou `legislacao`) e percorrer `README.md` raiz -> `README.md` tematico.
3. Selecionar 3 a 8 documentos candidatos conforme escopo.
4. Ler secoes centrais: definicoes, requisitos, competencia, prazos, fluxo, excecoes e revogacoes/alteracoes (quando houver).
5. Responder sem inferencias sem fonte e com rastreabilidade explicita.
6. Encerrar com referencias dos arquivos usados.

## Additional Rules For Normative Questions

Quando a pergunta envolver atos normativos (artigo, prazo legal, competencia, revogacao/alteracao, conflito de normas), aplicar tambem:

1. **Vigencia primeiro**: priorizar o ato mais recente aplicavel ao tema.
2. **Ato alterador prevalece**: quando houver "altera", "retifica", "revoga" ou "consolida", considerar a redacao vigente.
3. **Especialidade sobre generalidade**: norma especifica do tema prevalece sobre regra geral, salvo conflito hierarquico explicito.
4. **Nivel federativo**: em temas nacionais, confrontar normas internas da UFMS com atos nacionais aplicaveis.
5. **Temporalidade explicita**: informar data do ato e, quando houver, data de entrada em vigor.

Caso de alta criticidade (graduacao):

- Tratar `Resolucao Cograd n. 430/2021` em conjunto com `Resolucao Cograd n. 1.213/2025`.
- Considerar que a `Resolucao Cograd n. 1.213/2025` altera dispositivos da `Resolucao Cograd n. 430/2021` e define entrada em vigor em 02/03/2026 para as alteracoes indicadas.
- Sempre verificar se a pergunta se refere a periodo anterior ou posterior a entrada em vigor.

## Required Response Format

A resposta ao usuario deve conter:

- **Conclusao objetiva** (1-3 frases).
- **Fundamentacao**:
  - documento-base (arquivo, tipo e data, quando houver);
  - dispositivo(s) relevante(s) quando aplicavel (artigo, item, secao);
  - trecho citado (1-2 linhas) do trecho usado;
  - condicao de vigencia/temporalidade quando aplicavel.
- **Referencias**:
  - links clicaveis dos arquivos usados no repositorio (Markdown).
  - para consulta normativa, incluir preferencialmente os atos principais e alteradores.
- **Limites**:
  - declarar lacuna, conflito, ausencia documental no acervo, ou necessidade de fonte externa.

## Pre-Answer Checklist

Antes de finalizar, confirme:

- [ ] Consultei apenas `docs/` fora de `docs/faq/`.
- [ ] Passei por `README.md` da pasta raiz e da subpasta relevante antes do documento final.
- [ ] Citei o(s) arquivo(s) especifico(s) que fundamentam a conclusao.
- [ ] Para tema normativo, verifiquei vigencia e cadeia de alteracoes.
- [ ] Considerei recorte temporal da pergunta quando aplicavel.
- [ ] Listei links clicaveis dos arquivos usados.
- [ ] Declarei limites quando houver incerteza documental.

## Do Not Do

- Nao responder apenas com base no nome do arquivo.
- Nao usar `docs/faq/` como fundamento documental primario.
- Nao usar resumo de `README.md` como se fosse texto integral do documento final.
- Nao omitir conflitos entre documentos relevantes.
- Nao afirmar alteracao ou revogacao sem citar o documento alterador.
- Nao inventar artigo, prazo, competencia, fluxo ou requisito.

## Short Output Template

Use este modelo:

1) Conclusao objetiva:
<1-3 frases>

2) Fundamentacao:

- <documento-base, tipo, data>
- <artigo/item/dispositivo, quando aplicavel>
- `trecho citado do documento`
- <vigencia/temporalidade, quando aplicavel>

3) Referencias:

- [arquivo-1](link-relativo-1)
- [arquivo-2](link-relativo-2)

4) Limites:

- <se houver lacuna, conflito ou fonte externa necessaria>
