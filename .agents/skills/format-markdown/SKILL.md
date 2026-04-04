---
name: format-markdown
description: Valida e orienta formatacao de documentos Markdown com markdownlint-cli2. Use sempre que o usuario pedir checagem de padrao, revisao de estilo Markdown ou validacao antes de publicar documentacao.
---

Esta skill valida documentos Markdown com `markdownlint-cli2` usando o script
manual do projeto.

## Quando usar

Use esta skill quando o usuario pedir para:

- validar a formatacao de arquivos `.md`;
- checar problemas de estilo em documentacao;
- confirmar conformidade antes de entrega/publicacao.

## Fluxo

1. Executar validacao na raiz do repositorio:

```bash
npm run lint:md
```

1. Se houver erros, reportar de forma acionavel:
   - arquivo;
   - linha;
   - regra (ex.: `MD013`);
   - ajuste recomendado.

1. Se nao houver erros, confirmar que os documentos passaram na validacao.

## Referencias no projeto

- Script: `package.json` -> `lint:md`
- Configuracao: `.markdownlint-cli2.jsonc`
