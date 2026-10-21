-- Aula 10: CASE, CTE e funções de janela
-- Eu faço: faixas de ticket com CASE
SELECT CASE
         WHEN valor_total < 30  THEN '1. até R$ 30'
         WHEN valor_total < 100 THEN '2. R$ 30 a 100'
         WHEN valor_total < 300 THEN '3. R$ 100 a 300'
         ELSE                        '4. acima de R$ 300'
       END AS faixa,
       COUNT(*) AS n_vendas,
       ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
WHERE data LIKE '2025%'
GROUP BY faixa
ORDER BY faixa;

-- Fazemos juntos: meta × realizado com CTE
WITH realizado AS (
    SELECT SUBSTR(data, 1, 7) AS ano_mes, SUM(valor_total) AS realizado
    FROM vendas
    GROUP BY ano_mes
)
SELECT r.ano_mes,
       m.meta,
       ROUND(r.realizado, 2)                 AS realizado,
       ROUND(100.0 * r.realizado / m.meta, 1) AS pct_meta,
       CASE WHEN r.realizado >= m.meta THEN 'Bateu' ELSE 'Não bateu' END AS situacao
FROM realizado AS r
JOIN metas_mensais AS m ON m.ano_mes = r.ano_mes
WHERE r.ano_mes LIKE '2025%'
ORDER BY r.ano_mes;

-- Você faz 1: acumulado diário de julho/2025 (a "coluna ACUMULADO" da planilha de metas)
WITH dia AS (
    SELECT data, SUM(valor_total) AS fat
    FROM vendas
    WHERE data LIKE '2025-07%'
    GROUP BY data
)
SELECT data,
       ROUND(fat, 2) AS faturamento_dia,
       ROUND(SUM(fat) OVER (ORDER BY data), 2) AS acumulado
FROM dia
ORDER BY data;

-- Você faz 2: crescimento mês contra mês anterior (LAG)
WITH mes AS (
    SELECT SUBSTR(data, 1, 7) AS ano_mes, SUM(valor_total) AS fat
    FROM vendas
    GROUP BY ano_mes
)
SELECT ano_mes,
       ROUND(fat, 2) AS faturamento,
       ROUND(100.0 * (fat / LAG(fat) OVER (ORDER BY ano_mes) - 1), 1) AS var_mes_anterior_pct,
       ROUND(100.0 * (fat / LAG(fat, 12) OVER (ORDER BY ano_mes) - 1), 1) AS var_ano_anterior_pct
FROM mes
ORDER BY ano_mes;

-- Você faz 3: produto mais vendido (em R$) de cada categoria em 2025 (RANK)
WITH prod AS (
    SELECT p.categoria, p.produto, SUM(i.valor_item) AS fat
    FROM itens_venda AS i
    JOIN produtos AS p ON p.id_produto = i.id_produto
    JOIN vendas   AS v ON v.id_venda   = i.id_venda
    WHERE v.data LIKE '2025%'
    GROUP BY p.categoria, p.produto
),
ranqueado AS (
    SELECT *, RANK() OVER (PARTITION BY categoria ORDER BY fat DESC) AS posicao
    FROM prod
)
SELECT categoria, produto, ROUND(fat, 2) AS faturamento
FROM ranqueado
WHERE posicao = 1
ORDER BY faturamento DESC;
