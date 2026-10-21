-- Aula 07: SELECT, WHERE, ORDER BY
-- Eu faço
SELECT produto, categoria, preco_unitario
FROM produtos
WHERE categoria = 'Trufas'
ORDER BY preco_unitario DESC;

-- Fazemos juntos: vendas de Natal acima de R$ 300
SELECT id_venda, hora, canal, forma_pagamento, valor_total
FROM vendas
WHERE data = '2025-12-25'
  AND valor_total > 300
ORDER BY valor_total DESC;

-- Você faz 1: os 5 produtos com maior margem em R$
SELECT produto,
       preco_unitario,
       custo_unitario,
       ROUND(preco_unitario - custo_unitario, 2) AS margem
FROM produtos
ORDER BY margem DESC
LIMIT 5;

-- Você faz 2: vendas da Recepção pagas com Elo em julho/2025
SELECT id_venda, data, forma_pagamento, valor_total
FROM vendas
WHERE canal = 'Recepção'
  AND bandeira = 'Elo'
  AND data BETWEEN '2025-07-01' AND '2025-07-31'
ORDER BY data;

-- Você faz 3: produtos cujo nome contém "trufa" (maiúscula ou minúscula)
SELECT produto FROM produtos WHERE LOWER(produto) LIKE '%trufa%';
