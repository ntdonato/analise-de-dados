# Aula 08: GROUP BY, a tabela dinâmica do SQL

**Objetivo:** calcular faturamento, quantidade e ticket médio por mês, canal e forma de pagamento usando SQL.

**Tempo:** cerca de 2h30.

## Revisão rápida (Aula 07)

Antes de começar, responda de cabeça:
1. Em que ordem se escrevem SELECT, WHERE, FROM e ORDER BY?
2. Como pegar só as vendas de julho/2025?

## Analogia

Você já conhece: é a **tabela dinâmica** da Aula 02. O `GROUP BY` diz como separar os montinhos (linhas da tabela dinâmica), e as funções de agregação dizem o que calcular em cada montinho (área Valores).

| Tabela dinâmica | SQL |
|---|---|
| Linhas | `GROUP BY` |
| Valores: Soma | `SUM()` |
| Valores: Contagem | `COUNT()` |
| Valores: Média | `AVG()` |
| Valores: Mín/Máx | `MIN()`, `MAX()` |
| Filtro | `WHERE` (antes de agrupar) |
| Filtro de valores | `HAVING` (depois de agrupar) |

Onde a analogia quebra: no SQL, toda coluna do SELECT que **não** é uma agregação precisa estar no GROUP BY. A tabela dinâmica não exige isso porque você só arrasta campos.

## O que é de verdade

```sql
SELECT coluna_de_grupo, SUM(valor) AS total
FROM tabela
WHERE ...          -- filtra LINHAS antes de agrupar
GROUP BY coluna_de_grupo
HAVING SUM(valor) > 1000   -- filtra GRUPOS depois de agrupar
ORDER BY total DESC;
```

Funções úteis no SQLite:
- `SUBSTR(data, 1, 7)` pega os 7 primeiros caracteres de `2025-07-15`, ou seja, `2025-07` (o mês).
- `ROUND(x, 2)` arredonda para 2 casas.
- `COUNT(*)` conta linhas; `COUNT(DISTINCT coluna)` conta valores diferentes.

```
vendas (25 mil linhas) --WHERE 2025--> 13 mil linhas --GROUP BY mês--> 12 linhas
```

## Mão na massa

### Eu faço: faturamento por mês em 2025

```sql
SELECT SUBSTR(data, 1, 7)         AS ano_mes,
       COUNT(*)                   AS n_vendas,
       ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
WHERE data LIKE '2025%'
GROUP BY ano_mes
ORDER BY ano_mes;
```

Resultado esperado: 12 linhas. Confira com a tabela dinâmica da Aula 02: os valores devem ser iguais. Ver o mesmo número em duas ferramentas é uma ótima forma de validar.

### Fazemos juntos: ticket médio por forma de pagamento (2025)

```sql
SELECT forma_pagamento,
       COUNT(*)                   AS n_vendas,
       ROUND(___(valor_total), 2) AS ticket_medio
FROM vendas
WHERE data LIKE '2025%'
GROUP BY _______________
ORDER BY ticket_medio DESC;
```

### Você faz

1. Liste os **dias de 2025 com faturamento acima de R$ 8.000**. Use `HAVING`. Em que meses eles se concentram?
2. Faturamento **por ano e canal** (agrupe por duas colunas: `GROUP BY ano, canal`).
3. Desafio: quantos **dias diferentes** tiveram venda Online em 2025? (`COUNT(DISTINCT data)`)

## Checagem

1. Qual a diferença entre WHERE e HAVING? Dê um exemplo de cada com a tabela vendas.
2. Por que esta consulta dá erro (ou resultado estranho)? `SELECT canal, forma_pagamento, SUM(valor_total) FROM vendas GROUP BY canal;`
3. Como você usaria SQL para conferir o total de um fechamento de caixa?

## No seu portfólio

`minhas-consultas/aula-08.sql`. Commit: `Aula 08: agregações com GROUP BY`.

Próximo passo: Aula 09, juntar tabelas com JOIN.
