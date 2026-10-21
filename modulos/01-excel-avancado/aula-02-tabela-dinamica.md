# Aula 02: Tabela dinâmica

**Objetivo:** responder em 5 minutos "quanto vendemos por mês e por forma de pagamento?" usando 25 mil linhas, sem escrever nenhuma fórmula.

**Tempo:** cerca de 2 horas. **Arquivo:** `dados/loja.xlsx`, aba `vendas`.

Por que `.xlsx` e não o `.csv`? O CSV usa ponto como separador decimal (`148.8`). O Excel em português pode ler isso como 1488 ou como texto. O `loja.xlsx` tem os mesmos dados, já com números e datas no formato certo.

## Analogia

No fechamento de caixa, você pega uma pilha de comprovantes e separa em montinhos: crédito aqui, débito ali, PIX lá. Depois soma cada montinho.

A **tabela dinâmica** faz exatamente isso: você diz por qual critério separar os montinhos (linhas e colunas) e o que somar (valores). O Excel separa e soma sozinho. Se quiser separar de outro jeito, é só arrastar outro campo.

Onde a analogia quebra: a tabela dinâmica não muda os dados originais. Ela é só uma "visão" deles. Se os dados mudarem, você precisa clicar em **Atualizar**.

## O que é de verdade

Uma tabela dinâmica tem quatro áreas:

| Área | Pergunta que responde | Exemplo |
|---|---|---|
| Linhas | Separar por quê, de cima para baixo? | Mês |
| Colunas | Separar por quê, da esquerda para a direita? | Forma de pagamento |
| Valores | O que calcular? | Soma de valor_total |
| Filtros | Olhar só uma parte? | Ano = 2025 |

Regra que evita 90% dos problemas: **transforme os dados em Tabela antes** (Ctrl+Alt+T). Assim a tabela dinâmica cresce sozinha quando entram linhas novas.

## Mão na massa

### Eu faço: faturamento por mês

1. Abra `loja.xlsx` e salve uma cópia como `aula-02.xlsx` (assim o original fica intacto).
2. Na aba `vendas`, os dados já estão numa Tabela chamada `tbVendas` (confira em `Design da Tabela`). Num arquivo seu, sem Tabela, você criaria clicando numa célula e apertando **Ctrl+Alt+T**.
3. Clique dentro da Tabela e vá em `Inserir > Tabela Dinâmica > Nova planilha`.
4. Arraste `data` para **Linhas**. O Excel agrupa sozinho em Anos, Trimestres e Meses. Se não agrupar: clique com o botão direito numa data > **Agrupar** > marque Meses e Anos.
5. Arraste `valor_total` para **Valores**. Ele vira "Soma de valor_total".
6. Formate: botão direito no valor > **Formato do Número** > Moeda.

O que você deve ver: 2024 e 2025, cada um com 12 meses. Dezembro é sempre o maior mês.

### Fazemos juntos: participação de cada forma de pagamento

Complete os passos:

1. Arraste `forma_pagamento` para ______ (área que separa da esquerda para a direita).
2. Coloque `data` (Anos) em **Filtros** e escolha 2025.
3. No valor, botão direito > **Mostrar Valores Como** > ______ (opção que transforma em porcentagem do total).

Pergunta: qual forma de pagamento responde por mais dinheiro em 2025? E qual a fatia do PIX?

### Você faz

Descubra **em qual dia da semana a loja fatura mais**.

Dica: a base não tem a coluna "dia da semana". Crie na Tabela uma coluna `dia_semana` com a fórmula `=TEXTO([@data];"dddd")`. Depois atualize a tabela dinâmica (`Analisar > Atualizar`).

Resultado esperado: os três maiores dias são próximos entre si, e muito acima de segunda-feira.

## Checagem

1. Por que vale criar uma Tabela (Ctrl+Alt+T) antes da tabela dinâmica?
2. Você incluiu as vendas de janeiro/2026 na base e a tabela dinâmica não mudou. O que faltou?
3. O gerente pergunta: "o canal Online vale a pena?" Que tabela dinâmica você montaria para começar a responder?

As respostas estão em `gabarito.md`. Responda antes de olhar.

## No seu portfólio

Salve o arquivo como `modulos/01-excel-avancado/meus-arquivos/aula-02.xlsx`, com uma aba por exercício. Commit: `Aula 02: tabelas dinâmicas de vendas`.

Próximo passo: Aula 03, montar a planilha de metas × realizado com PROCX e SOMASES.
