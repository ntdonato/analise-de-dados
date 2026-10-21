# Gabarito: Módulo 3 (SQL)

As consultas completas estão nos arquivos `aula-07.sql` a `aula-10.sql` desta pasta. Aqui estão os resultados para conferir e as respostas da checagem.

## Aula 07
- Fazemos juntos: `data = '2025-12-25'`, `valor_total > 300`, `ORDER BY valor_total DESC`. São 4 vendas, a maior de R$ 503,13.
- Você faz 1: Kit presente grande (R$ 152,90), Cesta café colonial (R$ 127,90), Kit presente médio (R$ 91,90), Fondue kit (R$ 77,90), Kit presente pequeno (R$ 53,90).
- Você faz 2: 13 vendas.
- Você faz 3: 6 produtos (inclui "Panetone trufado").

Checagem
1. WHERE escolhe **quais** linhas entram; ORDER BY só muda a **ordem** em que aparecem.
2. Sem aspas, o banco entende `2025-12-25` como a conta 2025 menos 12 menos 25 = 1988.
3. `WHERE canal = 'Loja' AND forma_pagamento IN ('Débito', 'Crédito')`. Sem parênteses, `canal = 'Loja' AND forma_pagamento = 'Débito' OR forma_pagamento = 'Crédito'` traria crédito de **todos** os canais, porque o AND é avaliado antes do OR.

## Aula 08
- Fazemos juntos: `AVG(valor_total)` e `GROUP BY forma_pagamento`. Os tickets ficam todos entre R$ 97,89 e R$ 102,59.
- Você faz 1: 9 dias, todos em novembro e dezembro de 2025. O maior foi 06/12/2025 (R$ 11.017,72).
- Você faz 2: Loja R$ 1.023.873,13 · Recepção R$ 179.448,73 · Online R$ 106.129,56 (2025).

Checagem
1. WHERE filtra linhas antes de agrupar (ex.: só 2025). HAVING filtra grupos depois (ex.: só os dias com soma > 8.000).
2. `forma_pagamento` não está no GROUP BY nem dentro de uma agregação. Bancos como PostgreSQL dão erro; o SQLite devolve um valor qualquer da forma de pagamento, o que é pior porque parece certo.
3. `SELECT forma_pagamento, SUM(valor_total) FROM vendas WHERE data = 'AAAA-MM-DD' GROUP BY forma_pagamento;` e comparar com o relatório do caixa.

## Aula 09
- Eu faço: Kits Presente R$ 342.808,94 · Chocolates R$ 265.116,72 · Trufas R$ 242.688,36 · Sazonais R$ 168.744,68 · Cafeteria R$ 125.532,80 · Souvenirs R$ 102.888,59 · Bebidas R$ 61.671,33.
- Fazemos juntos: `quantidade`, `id_produto`, `id_venda`, `LIMIT 10`. Líder: Caixa 12 trufas (R$ 131.816,51).
- Você faz 1: maior margem %: **Cafeteria (68,1%)**. Maior lucro em R$: **Kits Presente (R$ 205.218,94)**.
- Você faz 2: Ovo de Páscoa e Panetone trufado. Faz sentido: são sazonais (Páscoa e Natal).

Checagem
1. JOIN traz só o que tem par nas duas tabelas; LEFT JOIN traz tudo da esquerda, mesmo sem par (com NULL na direita).
2. Porque cada venda se repete uma vez por item. Uma venda de R$ 100 com 3 itens seria somada 3 vezes (R$ 300).
3. Depende do objetivo: para decidir o que **promover**, importa o lucro em R$; para decidir **preço** ou se vale manter um produto, importa a margem %.

## Aula 10
- Faixas (2025): até R$ 30: 3.711 vendas · R$ 30–100: 4.743 · R$ 100–300: 3.944 · acima de R$ 300: 632 vendas que trazem R$ 251.946,66 (19% do faturamento).
- Meta × realizado: 6 meses batidos em 2025 (mesmo resultado da Aula 03).
- Acumulado de julho/2025: termina em R$ 145.724,00 no dia 31.
- YoY: jan/2025 +13,4% e dez/2025 +11,4% (igual à Aula 06).
- Campeões: Caixa 12 trufas, Panetone trufado, Kit presente grande, Barra ao leite 300g, Pelúcia mascote, Fatia de torta, Vinho espumante moscatel.

Checagem
1. Com GROUP BY, os dias viram uma linha só (o total). Com OVER, cada dia continua sendo uma linha, e ganha uma coluna com a soma até ele.
2. Porque não existe linha anterior à primeira.
3. "É o quanto já vendemos no mês até cada dia. Dá para ver em que dia passamos da metade da meta e se o ritmo está bom."
