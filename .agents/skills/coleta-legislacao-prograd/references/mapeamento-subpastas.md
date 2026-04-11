# Mapeamento de subpastas da legislacao

Este mapeamento orienta a classificacao de documentos coletados da PROGRAD para `{root}/assets/`.

| Prefixo da pagina de origem | Destino local |
| --- | --- |
| `https://prograd.ufms.br/legislacao/legislacao-avaliacao/` | `{root}/assets/legislacao-avaliacao` |
| `https://prograd.ufms.br/legislacao/legislacao-educacional-nacional/` | `{root}/assets/legislacao-educacional-nacional` |
| `https://prograd.ufms.br/legislacao/legislacao-estagio/` | `{root}/assets/legislacao-estagio` |
| `https://prograd.ufms.br/legislacao/legislacao-formacao-de-professores/` | `{root}/assets/legislacao-formacao-de-professores` |
| `https://prograd.ufms.br/legislacao/legislacao-geral-da-ufms/` | `{root}/assets/legislacao-geral-da-ufms` |
| `https://prograd.ufms.br/legislacao/legislacao-geral-graduacao/` | `{root}/assets/legislacao-geral-graduacao` |
| `https://prograd.ufms.br/legislacao/legislacao-ingresso/` | `{root}/assets/legislacao-ingresso` |
| `https://prograd.ufms.br/legislacao/legislacao-professor-substituto/` | `{root}/assets/legislacao-professor-substituto` |
| `https://prograd.ufms.br/legislacao/normas/` | `{root}/assets/normas` |
| `https://prograd.ufms.br/regulamentos-de-ccnd-da-graduacao/` | `{root}/assets/regulamentos-de-ccnd-da-graduacao` |
| `https://prograd.ufms.br/legislacao/regulamentos-de-ccnd-da-graduacao/` | `{root}/assets/regulamentos-de-ccnd-da-graduacao` |
| `https://prograd.ufms.br/programas/programa-de-estudantes-convenio-de-graduacao-pec-g/` | `{root}/assets/programas/programa-de-estudantes-convenio-de-graduacao-pec-g` |
| `https://prograd.ufms.br/a-prograd/digac/programa-de-estudantes-convenio-de-graduacao-pec-g/` | `{root}/assets/programas/programa-de-estudantes-convenio-de-graduacao-pec-g` |
| `https://prograd.ufms.br/legislacao/legislacao-programa-de-educacao-tutorial/` | `{root}/assets/programas` |
| `https://prograd.ufms.br/programas-e-projetos/programa-de-educacao-tutorial-pet/` | `{root}/assets/programas` |
| `https://prograd.ufms.br/legislacao/legislacao-monitoria/` | `{root}/assets/programas` |
| `https://prograd.ufms.br/programas-e-projetos/projeto-de-ensino-de-graduacao/` | `{root}/assets/programas` |

## Regras de fallback

- Se a origem for `https://prograd.ufms.br/legislacao/normas/`, priorize `{root}/assets/normas`.
- Se a URL de origem estiver em dominio legado `preg.bellatrix.ufms.br`, a coleta usa fallback de TLS inseguro por padrao para recuperar o arquivo.
- Se nao houver prefixo mapeado, aplicar fallback por palavras-chave no URL/pagina (ex.: `pec-g`, `resolucao-cograd-n-430`, `monitoria`, `pet`, `projeto-de-ensino-de-graduacao`).
- Para novos arquivos PDF diretos, manter o nome original do arquivo na URL final.
- Para links de boletim oficial, usar como padrao `BOLETIMOFICIAL-id-<id>.pdf`.
- Se houver ambiguidade de mapeamento, manter documento em pasta candidata mais especifica e registrar pendencia no relatorio.
- Se nao houver mapeamento, registrar como `sem-mapeamento` e nao mover arquivos existentes.
