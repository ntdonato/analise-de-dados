-- Aula 08: GROUP BY e agregações
-- Eu faço: faturamento por mês em 2025
SELECT SUBSTR(data, 1, 7)        AS ano_mes,
       COUNT(*)                  AS n_vendas,
       ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
WHERE data LIKE '2025%'
GROUP BY ano_mes
ORDER BY ano_mes;

-- Fazemos juntos: ticket médio por forma de pagamento em 2025
SELECT forma_pagamento,
       COUNT(*)                   AS n_vendas,
       ROUND(AVG(valor_total), 2) AS ticket_medio
FROM vendas
WHERE data LIKE '2025%'
GROUP BY forma_pagamento
ORDER BY ticket_medio DESC;

-- Você faz 1: dias de 2025 com faturamento acima de R$ 8.000
SELECT data, ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
WHERE data LIKE '2025%'
GROUP BY data
HAVING SUM(valor_total) > 8000
ORDER BY faturamento DESC;

-- Você faz 2: faturamento por canal e ano
SELECT SUBSTR(data, 1, 4) AS ano, canal, ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
GROUP BY ano, canal
ORDER BY ano, faturamento DESC;
