---
name: criacao-faq-coordenacao
description: Cria e revisa FAQs institucionais para coordenacao de curso com analise criteriosa, rastreabilidade e foco operacional. Use esta skill sempre que o usuario pedir FAQ, perguntas frequentes, guia de atendimento, respostas padrao de secretaria/coordenacao, ou transformar normas/procedimentos em linguagem clara e acionavel.
---

# Skill: Criacao de FAQ para Coordenacao de Curso

Esta skill estrutura a elaboracao de FAQs com profundidade analitica, evitando respostas superficiais e sem base documental.

## Objetivo da skill

Produzir FAQs que sejam:
- **claras** para o publico final;
- **corretas** em relacao a norma/procedimento;
- **acionaveis** para atendimento;
- **rastreaveis** (com links de arquivo clicaveis);
- **reutilizaveis** entre coordenacao, secretaria e docentes.

## Quando usar

Use quando houver pedido de:
- criacao de FAQ do zero;
- revisao/atualizacao de FAQ existente;
- padronizacao de respostas frequentes da coordenacao;
- conversao de norma em orientacao para estudante.

Nao use para responder consulta normativa sem verificar os atos. Se houver duvida sobre artigo, prazo, competencia, vigencia, alteracao/revogacao ou conflito entre normas, carregue a skill [`ufms-legislacao`](../ufms-legislacao/SKILL.md) e siga seu fluxo.

## Profundidade minima obrigatoria (analise criteriosa)

Antes de redigir o FAQ final, execute estas 7 etapas:

1. **Definir escopo da demanda**
   - Tema central e limites (ex.: regime especial na graduacao, nao pos-graduacao).
   - Periodo de interesse (importante para vigencia).

2. **Mapear publico e decisores**
   - Quem pergunta (estudante, docente, secretaria).
   - Quem analisa/decide (coordenacao, colegiado, pro-reitoria).

3. **Levantamento de fontes**
   - Ler indice e README(s) relevantes antes dos atos completos.
   - Selecionar normas principais e, se houver, atos alteradores.

4. **Validar vigencia e cadeia de alteracoes**
   - Confirmar se o ato esta vigente.
   - Confirmar alteracoes, retificacoes, revogacoes e consolidacoes.
   - Declarar limite quando nao for possivel comprovar cadeia completa.

5. **Extrair regras operacionais**
   - Elegibilidade (quem pode solicitar).
   - Condicoes de aplicacao.
   - Prazos e marcos de contagem.
   - Documentos obrigatorios.
   - Fluxo de tramitacao (protocolo -> analise -> decisao -> comunicacao).
   - Consequencias de deferimento e indeferimento.

6. **Identificar pontos de risco de interpretacao**
   - Termos ambíguos.
   - Excecoes e casos limítrofes.
   - Dependencia de norma externa nao presente no acervo.

7. **So entao redigir o FAQ final**
   - Linguagem simples, sem perder exatidao normativa.
   - Cada resposta deve orientar o proximo passo pratico.

## Matriz obrigatoria de rastreabilidade (pergunta -> dispositivo)

Antes de finalizar, monte obrigatoriamente uma matriz com:
- Pergunta da FAQ;
- Regra sintetizada em 1 frase;
- Dispositivo de base (ato + artigo/paragrafo/inciso);
- Trecho-chave da norma (1-2 linhas, quando houver).

Sem essa matriz, a FAQ nao deve ser considerada pronta.

## Criterios de completude minima (Gate de qualidade)

Considere a FAQ **aprovada** somente quando atingir todos os itens abaixo:

1. **Cobertura funcional**: responde quem pode solicitar, condicoes, prazo, documentos, protocolo, analise/decisao e indeferimento.
2. **Rastreabilidade**: toda resposta normativa aponta base documental.
3. **Acionabilidade**: cada resposta deixa explicito o proximo passo do leitor.
4. **Temporalidade**: vigencia e recorte temporal foram verificados (quando aplicavel).
5. **Clareza**: sem jargao desnecessario e sem ambiguidade relevante.

Se qualquer item falhar, revisar antes de entregar.

## Estrutura de saida obrigatoria

Entregue nesta ordem:

1. **Analise previa resumida**
   - Escopo
   - Publico-alvo
   - Matriz de regras (quem/prazo/documentos/decisao)
   - Matriz de rastreabilidade (pergunta -> dispositivo)
   - Riscos e limites

2. **FAQ final (Markdown)**
   - Use [`references/TEMPLATE_FAQ.md`](references/TEMPLATE_FAQ.md)

3. **Observacoes de aplicacao**
   - O que a coordenacao pode customizar localmente (contatos, canais, formulários).

4. **Referencias de base**
   - Links clicaveis (Markdown) dos arquivos usados.
   - Referencie diretamente os documentos normativos aplicados (ex.: PDFs), sem incluir `README.md` na lista final de referencias.
   - Para PDFs, use o **titulo do PDF** como texto do link (ex.: `[RESOLUCAO (COGRAD) n 430_ de 16-12-2021.](caminho/arquivo.pdf)`).
   - Para arquivos nao-PDF que forem indispensaveis, use o nome do arquivo como texto do link.

5. **Limites**
   - Lacunas documentais, necessidade de fonte externa, conflitos nao resolvidos.

## Destino dos arquivos gerados

Ao salvar entregaveis finais, usar sempre [`faq/<tema>/`](../../../faq/).

Padrao recomendado de nome:
- [`faq/<tema>/FAQ_<TEMA>.md`](../../../faq/)
- [`faq/<tema>/ANALISE_<TEMA>.md`](../../../faq/) (quando a analise for separada)

## Regras de redacao

- Perguntas em linguagem natural (como o usuario realmente pergunta).
- Respostas entre 3 e 8 linhas, objetivas.
- Destaque prazos em **negrito**.
- Liste documentos e passos em bullets quando aplicavel.
- Use condicional explicita: "Se X, entao Y".
- Evite frases vagas como "procure o setor responsavel" sem indicar proximo passo.
- Inclua, sempre que possivel, a linha **Base:** ao final de cada resposta normativa.
- Quando houver dispositivo normativo, prefira citar artigo/paragrafo/inciso de forma completa.

## Checklist de qualidade antes de finalizar

- [ ] A conclusao de cada resposta bate com a fonte?
- [ ] Prazo, marco de contagem e excecoes estao claros?
- [ ] O leitor sabe exatamente o que fazer agora?
- [ ] Linguagem sem jargao desnecessario?
- [ ] Referencias com links clicaveis foram listadas, usando o titulo do PDF como texto do link quando aplicavel e sem `README.md`?
- [ ] Limites e incertezas foram explicitados?
- [ ] A matriz pergunta->dispositivo foi preenchida?
- [ ] A FAQ passou no Gate de completude minima?

## Iteracao curta obrigatoria (teste -> ajuste -> reteste)

Quando esta skill for criada/atualizada, execute um ciclo minimo:

1. **Teste inicial** com 2-3 prompts realistas de coordenacao.
2. **Diagnostico**: registrar falhas por criterio (cobertura, rastreabilidade, acionabilidade, clareza).
3. **Ajuste da skill/templates** para corrigir as falhas.
4. **Reteste** com os mesmos prompts e comparar melhoria.

Formato de registro sugerido:
- Iteracao 1 (baseline): pontos fortes, falhas, decisoes de ajuste.
- Iteracao 2 (apos ajuste): o que melhorou, o que falta.

So considerar a skill pronta quando a iteracao 2 atender integralmente o Gate de completude minima.

## Organizacao de arquivos

- **Documentos FAQ gerados para uso institucional**: salvar em [`faq/`](../../../faq/) (nao misturar com arquivos da skill).

## Recursos da skill

- [`references/TEMPLATE_ANALISE_FAQ.md`](references/TEMPLATE_ANALISE_FAQ.md)
- [`references/TEMPLATE_FAQ.md`](references/TEMPLATE_FAQ.md)
