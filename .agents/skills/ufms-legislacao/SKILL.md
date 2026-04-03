---
name: ufms-legislacao
description: Diretrizes para consultas normativas no acervo legislacao, com foco em vigencia, cadeia de alteracoes e rastreabilidade de resposta. Use sempre que houver duvidas sobre artigo, prazo, competencia, revogacao/alteracao, ou conflito entre atos internos da UFMS e normas nacionais (MEC/CNE).
---

# UFMS Legislacao

Esta skill orienta consultas, interpretacao e respostas sobre normas do acervo [`legislacao`](../../../legislacao/), priorizando precisao normativa, vigencia e citacao rastreavel.

## When to Use This Skill

Use esta skill quando o usuario:
- perguntar sobre regras, prazos, competencias, procedimentos ou direitos/deveres regulados por normas da UFMS;
- pedir interpretacao de resolucoes, instrucoes normativas, regulamentos ou atos correlatos;
- precisar de resposta com base em artigo/dispositivo e estado de vigencia.

Nao use esta skill para opinioes sem base normativa, ou quando o tema exigir fonte externa nao disponivel no acervo (nesses casos, declarar limite).

## Mandatory Input Rule

Siga obrigatoriamente esta ordem:
1. Iniciar por [`legislacao/README.md`](../../../legislacao/README.md).
2. Identificar subpasta(s) relevante(s) pelo indice.
3. Abrir o `README.md` da subpasta antes de ler PDFs (ex.: [`legislacao/legislacao-geral-graduacao/README.md`](../../../legislacao/legislacao-geral-graduacao/README.md)).
4. Carregar no contexto apenas arquivos potencialmente relevantes para a pergunta.

Excecao: se o usuario indicar expressamente um arquivo normativo especifico, voce pode iniciar por ele; ainda assim, valide no `README.md` da pasta (ex.: [`legislacao/normas/README.md`](../../../legislacao/normas/README.md)) para confirmar contexto, vigencia e possiveis atos alteradores.

## Quick Topic Map

- [`legislacao-geral-da-ufms/`](../../../legislacao/legislacao-geral-da-ufms/): estatuto, regimento e atos institucionais gerais.
- [`legislacao-geral-graduacao/`](../../../legislacao/legislacao-geral-graduacao/): regulamento geral da graduacao, ingresso, matricula, avaliacao, integralizacao.
- [`normas/`](../../../legislacao/normas/): instrucoes normativas (procedimentos operacionais da Prograd e conjuntas).
- [`legislacao-estagio/`](../../../legislacao/legislacao-estagio/): estagio obrigatorio/nao obrigatorio e alteracoes historicas.
- [`legislacao-ingresso/`](../../../legislacao/legislacao-ingresso/): Sisu, cotas, mobilidade e ingresso.
- [`legislacao-avaliacao/`](../../../legislacao/legislacao-avaliacao/): regulacao e avaliacao institucional/curso (e-MEC, credenciamento).
- [`legislacao-educacional-nacional/`](../../../legislacao/legislacao-educacional-nacional/): marcos nacionais (MEC/CNE/CONAES).
- [`legislacao-formacao-de-professores/`](../../../legislacao/legislacao-formacao-de-professores/): formacao inicial e continuada de docentes.
- [`legislacao-professor-substituto/`](../../../legislacao/legislacao-professor-substituto/): selecao/solicitacao de professor substituto.
- [`programas/`](../../../legislacao/programas/) e subpastas: normas de programas especificos (ex.: PEC-G).
- [`regulamentos-de-ccnd-da-graduacao/`](../../../legislacao/regulamentos-de-ccnd-da-graduacao/): regulamentos especificos de componentes/cursos.

## Normative Prioritization Rules

1. **Vigencia primeiro**: priorizar o ato mais recente aplicavel ao tema.
2. **Ato alterador prevalece**: quando houver "altera", "retifica", "revoga" ou "consolida", considerar a redacao vigente.
3. **Especialidade sobre generalidade**: norma especifica do tema prevalece sobre regra geral, salvo conflito hierarquico explicito.
4. **Nivel federativo**: em temas nacionais, confrontar normas internas da UFMS com atos nacionais aplicaveis.
5. **Temporalidade explicita**: informar data do ato e, quando houver, data de entrada em vigor.

## Critical Validity Rule (Graduation)

Caso de alta criticidade (graduacao):
- Tratar `Resolucao Cograd n. 430/2021` em conjunto com `Resolucao Cograd n. 1.213/2025`.
- Considerar que a `Resolucao Cograd n. 1.213/2025` altera dispositivos da `Resolucao Cograd n. 430/2021` e define entrada em vigor em 02/03/2026 para as alteracoes indicadas.
- Sempre verificar se a pergunta se refere a periodo anterior ou posterior a entrada em vigor.

## Standard Consultation Workflow

1. Classificar a pergunta (tema principal + temas secundarios).
2. Navegar pelos `README.md` (raiz -> subpasta), iniciando por [`legislacao/README.md`](../../../legislacao/README.md) e seguindo para o `README.md` tematico aplicavel.
3. Selecionar 3 a 8 documentos candidatos conforme escopo.
4. Ler ementa, cabecalho e dispositivos centrais (definicoes, competencia, prazos, revogacoes).
5. Confirmar vigencia e cadeia de alteracoes.
6. Responder com base em artigo/dispositivo, sem inferencias sem fonte normativa.
7. Encerrar com referencias dos arquivos usados.

## Required Response Format

A resposta ao usuario deve conter:

- **Conclusao objetiva** (1-3 frases).
- **Fundamentacao**:
  - ato normativo (tipo, numero, data);
  - artigo(s)/dispositivo(s) relevantes;
  - trecho citado (1-2 linhas) do dispositivo utilizado;
  - condicao de vigencia (quando aplicavel).
- **Referencias**:
  - link clicavel do arquivo no repositorio (Markdown), preferencialmente relativo a `SKILL.md`.
- **Limites**:
  - declarar lacuna, conflito, ausencia de norma no acervo ou necessidade de fonte externa.

## Pre-Answer Checklist

Antes de finalizar, confirme:
- [ ] Verifiquei vigencia do ato aplicavel.
- [ ] Verifiquei alteracoes, retificacoes, revogacoes ou consolidacoes.
- [ ] Considerei recorte temporal da pergunta.
- [ ] Verifiquei hierarquia normativa (UFMS vs nacional) quando aplicavel.
- [ ] Citei dispositivo(s) especifico(s) que fundamentam a conclusao.
- [ ] Listei links clicaveis dos arquivos usados.
- [ ] Declarei limites quando houver incerteza documental.

## Best Practices

- Nao assumir revogacao tacita sem evidencia textual.
- Em cadeia de alteracoes, citar norma-base + norma alteradora.
- Em duvidas operacionais (procedimento/prazo), priorizar instrucoes normativas e dispositivos procedimentais vigentes.
- Em perguntas historicas, explicitar o marco temporal ("a epoca de...").

## Do Not Do

- Nao responder apenas com base no nome do arquivo.
- Nao usar resumo de `README.md` (ex.: [`legislacao/README.md`](../../../legislacao/README.md)) como se fosse texto normativo completo.
- Nao omitir conflitos entre atos.
- Nao afirmar alteracao ou revogacao sem citar o ato alterador (tipo, numero e data).
- Nao inventar artigo, prazo ou competencia.

## Short Output Template

Use este modelo:

1) Conclusao objetiva:
<1-3 frases>

2) Fundamentacao:
- <ato, numero, data>
- <artigo/dispositivo>
- <trecho citado do dispositivo>
- <vigencia/temporalidade>

3) Referencias:
- [<arquivo-1>](<link-relativo-1>)
- [<arquivo-2>](<link-relativo-2>)

4) Limites:
- <se houver lacuna, conflito ou fonte externa necessaria>
