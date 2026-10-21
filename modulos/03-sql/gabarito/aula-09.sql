-- Aula 09: JOIN
-- Eu faço: faturamento por categoria em 2025
SELECT p.categoria,
       ROUND(SUM(i.valor_item), 2) AS faturamento
FROM itens_venda AS i
JOIN produtos    AS p ON p.id_produto = i.id_produto
JOIN vendas      AS v ON v.id_venda   = i.id_venda
WHERE v.data LIKE '2025%'
GROUP BY p.categoria
ORDER BY faturamento DESC;

-- Fazemos juntos: top 10 produtos de 2025 por faturamento
SELECT p.produto,
       SUM(i.quantidade)           AS unidades,
       ROUND(SUM(i.valor_item), 2) AS faturamento
FROM itens_venda AS i
JOIN produtos    AS p ON p.id_produto = i.id_produto
JOIN vendas      AS v ON v.id_venda   = i.id_venda
WHERE v.data LIKE '2025%'
GROUP BY p.produto
ORDER BY faturamento DESC
LIMIT 10;

-- Você faz 1: margem bruta por categoria em 2025 (R$ e %)
SELECT p.categoria,
       ROUND(SUM(i.valor_item), 2)                                   AS receita,
       ROUND(SUM(i.quantidade * p.custo_unitario), 2)                AS custo,
       ROUND(SUM(i.valor_item) - SUM(i.quantidade * p.custo_unitario), 2) AS margem,
       ROUND(100.0 * (SUM(i.valor_item) - SUM(i.quantidade * p.custo_unitario)) / SUM(i.valor_item), 1) AS margem_pct
FROM itens_venda AS i
JOIN produtos    AS p ON p.id_produto = i.id_produto
JOIN vendas      AS v ON v.id_venda   = i.id_venda
WHERE v.data LIKE '2025%'
GROUP BY p.categoria
ORDER BY margem DESC;

-- Você faz 2 (LEFT JOIN): produtos que NÃO venderam em junho/2025
SELECT p.produto, p.categoria
FROM produtos AS p
LEFT JOIN (
    SELECT DISTINCT i.id_produto
    FROM itens_venda AS i
    JOIN vendas AS v ON v.id_venda = i.id_venda
    WHERE v.data LIKE '2025-06%'
) AS vendidos ON vendidos.id_produto = p.id_produto
WHERE vendidos.id_produto IS NULL;
