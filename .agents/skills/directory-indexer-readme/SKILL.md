---
name: directory-indexer-readme
description: Indexa qualquer diretorio apontado pelo usuario por meio de README.md mestre e READMEs de subpastas. Use sempre que o usuario pedir para indexar, catalogar, mapear, inventariar, organizar acervo, criar indice de documentos, ou atualizar READMEs de uma pasta especifica, mesmo que ele nao use a palavra "skill".
---

# Directory Indexer README

Esta skill padroniza indexacao documental para qualquer diretorio-alvo informado pelo usuario.

## Quando usar

Use esta skill quando o usuario:

- pedir indice de arquivos em uma pasta;
- pedir catalogacao de documentos por subpasta;
- pedir criacao/atualizacao de `README.md` para navegacao;
- pedir inventario com metadados e descricao curta por arquivo.

Nao use esta skill para interpretar conteudo normativo/juridico de merito. O foco aqui e indexacao e rastreabilidade documental.

## Regra de entrada obrigatoria

1. Identifique o diretorio-alvo explicitamente apontado pelo usuario.
2. Leia primeiro o `README.md` do diretorio-alvo, se existir.
3. Liste subpastas e arquivos do escopo.
4. Leia o `README.md` de cada subpasta, se existir, antes de recriar estrutura.

Se o usuario nao apontar caminho, solicite o caminho alvo antes de continuar.

## Escopo e seguranca

- Restrinja a indexacao ao diretorio informado.
- Nao mover, renomear ou apagar arquivos existentes sem pedido explicito.
- Nao inventar metadados tecnicos (data oficial, vigencia, status juridico) sem fonte no proprio documento.
- Declarar limites quando nao for possivel ler um arquivo ou inferir descricao confiavel.

## Fluxo padrao de trabalho

1. Classificar o objetivo: criar indice novo ou atualizar indice existente.
2. Mapear estrutura do diretorio (arquivos diretos + subpastas).
3. Gerar/atualizar `README.md` mestre no diretorio-alvo.
4. Gerar/atualizar `README.md` em cada subpasta relevante.
5. Validar consistencia:
   - links relativos funcionando;
   - contagem de cobertura coerente;
   - ids sem duplicacao no mesmo README;
   - secoes obrigatorias presentes.
6. Reportar o que foi indexado, o que ficou pendente e proximos ajustes recomendados.

## Estrutura obrigatoria do README mestre

Use este esqueleto:

```markdown
---
title: <nome-do-diretorio>
aliases:
  - indice <nome-do-diretorio>
tags:
  - indice
  - documentacao
tipo_documento: indice-mestre
escopo: <resumo do acervo>
ultima_revisao: <AAAA-MM-DD>
---

## <nome-do-diretorio>

<descricao curta do acervo>

## Como usar este indice

- <instrucao 1>
- <instrucao 2>

## Mapa tematico

| pasta | foco | termos de busca |
| --- | --- | --- |
| [subpasta-a](./subpasta-a/README.md) | <foco> | <termos> |

## Cobertura

- Total de arquivos diretos neste nivel: <n>
- Total de subpastas: <n>
- Criterio de organizacao: <criterio>
```

## Estrutura obrigatoria do README de subpasta

Use este esqueleto:

```markdown
---
title: <nome-da-subpasta>
tags:
  - indice
  - documentacao
tipo_documento: indice-tematico
tema: <tema da subpasta>
ultima_revisao: <AAAA-MM-DD>
---

## <nome-da-subpasta>

<descricao curta da subpasta>

## Consultas rapidas

- termos: <lista curta>
- tipos predominantes: <lista>

## Relacoes entre documentos (quando aplicavel)

| id | relacao | arquivo |
| --- | --- | --- |
| DOC-A | base para DOC-B | [arquivo-a.pdf](./arquivo-a.pdf) |

## Inventario de arquivos

Total de arquivos: <n>.

| id | arquivo | tipo | descricao | status |
| --- | --- | --- | --- | --- |
| DOC-001 | [arquivo.pdf](./arquivo.pdf) | pdf | <descricao objetiva> | catalogado |
```

## Regras de qualidade para descricoes

- Escrever descricoes objetivas, em 1 frase, focadas no papel do arquivo no acervo.
- Se o conteudo nao estiver legivel, usar descricao de limite: `arquivo identificado, leitura pendente`.
- Preferir `id` estavel baseado em nome do arquivo normalizado (sem espacos, em maiusculas, com hifens).

## Formato de saida da resposta ao usuario

Sempre entregar:

1) Diretorio indexado:

- `<caminho>`

1) Arquivos criados/atualizados:

- `<caminho/README.md>`

1) Cobertura:

- `<x>` subpastas indexadas
- `<y>` arquivos inventariados

1) Pendencias e limites:

- `<itens que exigem validacao humana>`

## Checklist final

- [ ] README mestre atualizado.
- [ ] READMEs de subpastas relevantes atualizados.
- [ ] Links relativos validados.
- [ ] Contagens de cobertura conferidas.
- [ ] Pendencias declaradas sem inferencia indevida.
