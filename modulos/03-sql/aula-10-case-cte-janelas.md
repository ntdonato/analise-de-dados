# Aula 10: CASE, CTE e funções de janela

**Objetivo:** recriar em SQL a sua planilha de metas: realizado × meta, % atingido, acumulado do mês e comparação com o mês anterior.

**Tempo:** cerca de 3h30. Esta é a aula mais densa do SQL. Pode dividir em dois dias.

## Revisão rápida

1. Para que serve o `LEFT JOIN`?
2. Por que somar `valor_total` depois de juntar com itens_venda é perigoso?

## Analogia

- **CASE** é o `SE` do Excel: "se o valor for menor que 30, escreva 'pequena'; senão...".
- **CTE** (`WITH`) é uma aba auxiliar. Você monta um resultado intermediário, dá um nome a ele e usa como se fosse uma tabela.
- **Função de janela** é a coluna ACUMULADO da sua planilha de metas: cada linha olha para as linhas vizinhas (as anteriores, o mês passado) **sem** juntar tudo numa linha só, como o GROUP BY faria.

Onde a analogia quebra: a CTE não fica salva no banco como uma aba. Ela existe só durante aquela consulta.

## O que é de verdade

### CASE
```sql
CASE
  WHEN condição1 THEN 'resultado1'
  WHEN condição2 THEN 'resultado2'
  ELSE 'senão'
END AS nova_coluna
```

### CTE
```sql
WITH nome AS (
    SELECT ...           -- consulta intermediária
)
SELECT ... FROM nome;    -- usa como tabela
```

### Funções de janela
```sql
FUNÇÃO() OVER (PARTITION BY grupo ORDER BY ordem)
```

| Função | Faz | Equivalente na planilha |
|---|---|---|
| `SUM(x) OVER (ORDER BY data)` | Soma acumulada | Coluna ACUMULADO |
| `LAG(x)` / `LAG(x, 12)` | Valor da linha anterior / de 12 linhas atrás | Mês anterior / mesmo mês do ano passado |
| `RANK() OVER (PARTITION BY categoria ORDER BY fat DESC)` | Posição dentro de cada grupo | "Top 1 de cada categoria" |

```
GROUP BY:  31 dias  ──►  1 linha (o total)
Janela:    31 dias  ──►  31 linhas, cada uma com o acumulado até ela
```

## Mão na massa

### Eu faço: faixas de ticket com CASE

```sql
SELECT CASE
         WHEN valor_total < 30  THEN '1. até R$ 30'
         WHEN valor_total < 100 THEN '2. R$ 30 a 100'
         WHEN valor_total < 300 THEN '3. R$ 100 a 300'
         ELSE                        '4. acima de R$ 300'
       END AS faixa,
       COUNT(*)                   AS n_vendas,
       ROUND(SUM(valor_total), 2) AS faturamento
FROM vendas
WHERE data LIKE '2025%'
GROUP BY faixa
ORDER BY faixa;
```

O número na frente do texto ("1.", "2.") é um truque para o ORDER BY colocar as faixas na ordem certa.

Leia o resultado: quantas vendas acima de R$ 300 existem, e quanto do faturamento elas trazem? Compare com o que você viu sobre outliers na Aula 05.

### Fazemos juntos: meta × realizado com CTE

```sql
WITH realizado AS (
    SELECT SUBSTR(data, 1, 7) AS ano_mes,
           SUM(valor_total)   AS realizado
    FROM vendas
    GROUP BY ano_mes
)
SELECT r.ano_mes,
       m.meta,
       ROUND(r.realizado, 2)                  AS realizado,
       ROUND(100.0 * r.realizado / m.meta, 1) AS pct_meta,
       CASE WHEN r.realizado >= m.meta THEN '_____' ELSE '_________' END AS situacao
FROM realizado AS r
JOIN __________ AS m ON m.ano_mes = r.ano_mes
WHERE r.ano_mes LIKE '2025%'
ORDER BY r.ano_mes;
```

Compare com a aba Painel da Aula 03. Devem bater.

Por que `100.0` e não `100`? Em alguns bancos, dividir inteiro por inteiro descarta as casas decimais. O `.0` força conta com decimais.

### Você faz

1. **Acumulado diário de julho/2025:** uma linha por dia, com o faturamento do dia e o acumulado do mês. (CTE com o total por dia + `SUM(...) OVER (ORDER BY data)`.)
2. **Variação mês a mês:** para cada mês de 2024 e 2025, mostre o faturamento, a variação % contra o mês anterior (`LAG(fat)`) e contra o mesmo mês do ano anterior (`LAG(fat, 12)`). Os números YoY batem com a Aula 06?
3. **Campeão de cada categoria:** o produto que mais faturou em cada categoria em 2025. Use `RANK() OVER (PARTITION BY categoria ORDER BY fat DESC)` numa CTE e filtre `posicao = 1`.

## Checagem

1. Qual a diferença entre `SUM(valor_total)` com GROUP BY e `SUM(valor_total) OVER (ORDER BY data)`?
2. Por que a primeira linha do `LAG` vem vazia (`NULL`)?
3. Explique, como para o gerente, o que a consulta do exercício 1 entrega.

## No seu portfólio

`minhas-consultas/aula-10.sql`. Commit: `Aula 10: CASE, CTE e funções de janela`.

Agora faça o **Projeto 1** (`projetos/p1-sql-analise-de-vendas/`). Ele é a prova de que você sabe SQL.
