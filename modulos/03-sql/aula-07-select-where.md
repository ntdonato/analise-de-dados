# Aula 07: SQL, primeiras perguntas ao banco de dados

**Objetivo:** abrir o banco da loja e escrever suas primeiras consultas: escolher colunas, filtrar linhas e ordenar.

**Tempo:** cerca de 2h30. **Arquivo:** `dados/loja.db`. **Ferramenta:** DB Browser for SQLite.

## Analogia

Lembra do arquivo de fichas dos hóspedes? Um **banco de dados** é esse arquivo, organizado em gavetas:

- cada gaveta é uma **tabela** (vendas, produtos, metas...);
- cada ficha é uma **linha** (uma venda);
- cada campo da ficha é uma **coluna** (data, valor, forma de pagamento).

**SQL** é a forma de pedir fichas ao arquivista. Você não abre a gaveta e procura com o dedo: você escreve o pedido, e ele devolve só o que você pediu.

Onde a analogia quebra: o arquivista do SQL nunca muda as fichas quando você só pergunta (SELECT). Pode perguntar à vontade, sem medo de estragar a base.

## O que é de verdade

SQL (*Structured Query Language*) é a linguagem padrão para consultar bancos de dados. É a ferramenta mais pedida nas vagas de dados. Uma consulta básica tem esta forma:

```sql
SELECT colunas        -- o que eu quero ver
FROM tabela           -- de qual gaveta
WHERE condição        -- só as fichas que...
ORDER BY coluna DESC  -- em que ordem
LIMIT 10;             -- quantas no máximo
```

A ordem de escrita é sempre essa. Linhas que começam com `--` são comentários (anotações que o banco ignora).

Operadores do WHERE:

| Operador | Exemplo |
|---|---|
| `=`, `<>`, `>`, `<`, `>=`, `<=` | `valor_total > 300` |
| `AND`, `OR`, `NOT` | `canal = 'Loja' AND forma_pagamento = 'PIX'` |
| `BETWEEN` | `data BETWEEN '2025-07-01' AND '2025-07-31'` |
| `IN` | `bandeira IN ('Visa', 'Elo')` |
| `LIKE` (`%` = qualquer coisa) | `produto LIKE 'Kit%'` |
| `IS NULL` | `valor_recebido IS NULL` |

Textos e datas vão entre aspas simples: `'Trufas'`, `'2025-12-25'`.

## Mão na massa

Prepare: instale o DB Browser for SQLite, clique em **Abrir banco de dados** e escolha `dados/loja.db`. Na aba **Estrutura do banco**, veja as tabelas. Depois vá à aba **Executar SQL**.

Rode uma consulta com **Ctrl+Enter** (ou F5).

### Eu faço

```sql
SELECT produto, categoria, preco_unitario
FROM produtos
WHERE categoria = 'Trufas'
ORDER BY preco_unitario DESC;
```

- `SELECT produto, categoria, preco_unitario`: quero só essas 3 colunas.
- `FROM produtos`: da tabela de produtos.
- `WHERE categoria = 'Trufas'`: só as linhas da categoria Trufas.
- `ORDER BY preco_unitario DESC`: do mais caro ao mais barato (`DESC` = decrescente; `ASC` = crescente, o padrão).

Resultado esperado: 6 produtos, com a caixa de 12 trufas no topo.

Experimente `SELECT * FROM vendas LIMIT 10;`. O `*` traz todas as colunas. Útil para espiar uma tabela, mas evite em consultas finais.

### Fazemos juntos

Liste as vendas do **dia de Natal de 2025 acima de R$ 300**, da maior para a menor. Complete:

```sql
SELECT id_venda, hora, canal, forma_pagamento, valor_total
FROM vendas
WHERE data = '__________'
  AND valor_total ___ 300
ORDER BY valor_total ____;
```

Resultado esperado: 4 vendas.

### Você faz

1. Os **5 produtos com maior margem em R$** (preço − custo). Dica: dá para criar uma coluna calculada no SELECT e dar nome a ela com `AS`:
   `ROUND(preco_unitario - custo_unitario, 2) AS margem`.
2. As vendas da **Recepção pagas com bandeira Elo em julho/2025**, por data.
3. Os produtos cujo nome contém "trufa", sem se importar com maiúsculas. Dica: `LOWER(produto) LIKE '%trufa%'`.

## Checagem

1. Qual a diferença entre `WHERE` e `ORDER BY`?
2. Por que `WHERE data = 2025-12-25` (sem aspas) não funciona?
3. Você quer as vendas de cartão de débito **ou** crédito da Loja. Escreva o WHERE. (Cuidado com AND e OR juntos: use parênteses ou `IN`.)

Gabarito: `gabarito/aula-07.sql` e `gabarito/respostas.md`.

## No seu portfólio

Salve suas consultas em `modulos/03-sql/minhas-consultas/aula-07.sql` (no DB Browser: botão **Salvar arquivo SQL**). Commit: `Aula 07: primeiras consultas SQL`.

Próximo passo: Aula 08, agrupar e somar com GROUP BY.
