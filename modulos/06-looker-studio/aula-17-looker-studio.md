# Aula 17: Looker Studio, o painel que abre por um link

**Objetivo:** montar no Looker Studio um painel de vendas com filtros e publicar um link que qualquer recrutador consegue abrir.

**Tempo:** cerca de 4 horas (inclui o Projeto 4). **Ferramenta:** lookerstudio.google.com (com a sua conta Google).

## Revisão rápida

1. Quais são os 4 cartões do seu dashboard no Power BI?
2. O que é uma medida, em uma frase?

## Analogia

Se o Power BI é um carro completo, com motor potente (DAX, modelo estrela), o Looker Studio é uma bicicleta elétrica: menos recursos, mas você sai pedalando em 5 minutos, ele roda no navegador e é fácil de emprestar. Basta mandar o link.

Você já usa Google Sheets todo dia, e o Looker Studio conversa direto com ele.

Onde a analogia quebra: a bicicleta não carrega muita gente. O Looker Studio fica lento com bases grandes e cálculos complexos, e não tem um modelo de relações tão forte quanto o Power BI.

## O que é de verdade

| Conceito | No Looker Studio |
|---|---|
| Fonte de dados | Google Sheets, CSV enviado, BigQuery e outras (chamadas de *conectores*) |
| Dimensão | Campo de texto ou data (verde) |
| Métrica | Campo numérico agregado (azul) |
| Campo calculado | Fórmula criada na fonte de dados |
| Combinação de dados | O "JOIN" do Looker (*blend*) |
| Controle | Filtro clicável (período, lista suspensa) |

## Mão na massa

### Eu faço: conectar os dados

1. No Google Drive, envie `dados/loja.xlsx` e abra com Google Sheets (`Abrir com > Planilhas Google`). Isso cria uma cópia em formato Google. (Use o `.xlsx`, não o `.csv`: com o Sheets em português, o ponto decimal do CSV pode virar texto.)
2. No Looker Studio: **Criar > Relatório > Google Sheets**, escolha a planilha e a aba `vendas`. Depois adicione outra fonte com a aba `metas_mensais`.
3. Clique em **Adicionar ao relatório**. Ele cria uma tabela automática. Apague.
4. Em **Recurso > Gerenciar fontes de dados > Editar**, confira os tipos: `data` como Data, `valor_total` como Moeda (BRL).

### Fazemos juntos: campos calculados e cartões

Na fonte de dados, clique em **Adicionar um campo**:

```
Nome: Ticket médio
Fórmula: SUM(valor_total) / COUNT(______)
```

Agora monte:
1. 3 **Visão geral** (cartões): soma de `valor_total`, contagem de `id_venda` e `Ticket médio`.
2. Nos cartões, ative **Comparação de períodos: Ano anterior**. O Looker calcula a variação sozinho, como o `Var % AA` que você fez com DAX.
3. Um **Controle de período** e um **Controle suspenso** com `canal`.

### Você faz

1. Gráfico de **série temporal** do faturamento por mês.
2. **Meta × realizado:** em `Recurso > Gerenciar combinações`, combine (blend) vendas com metas. Dica: crie em vendas um campo `ano_mes` com `FORMAT_DATETIME("%Y-%m", data)` e use-o como chave de junção com `metas_mensais.ano_mes`. Depois, faça um gráfico de colunas (realizado) com linha (meta).
3. Gráfico de barras por `forma_pagamento`, ordenado.
4. Use **Tema e layout** para aplicar as mesmas cores do seu Power BI. Um portfólio com a mesma identidade visual parece mais profissional.

### Publicar

Clique em **Compartilhar > Gerenciar acesso** e mude para **Qualquer pessoa com o link pode ver**. Copie o link para o README do Projeto 4. Abra numa janela anônima para testar se abre sem login.

## Checagem

1. Quando você escolheria o Looker Studio em vez do Power BI? E o contrário?
2. O que é um *blend* e qual conceito de SQL ele lembra?
3. Por que testar o link numa janela anônima?

## No seu portfólio

Siga o checklist do `projetos/p4-looker-studio/README.md`. Commit: `Projeto 4: painel de vendas no Looker Studio`.

Próximo passo: Aula 18, macros e VBA.
