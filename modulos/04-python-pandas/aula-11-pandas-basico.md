# Aula 11: Python com pandas, primeiros passos

**Objetivo:** abrir as 25 mil vendas no Google Colab, filtrar, ordenar e calcular faturamento e ticket médio com poucas linhas de código.

**Tempo:** cerca de 2h30. **Ferramenta:** Google Colab (no navegador, nada a instalar).

Você já fez o "Contador de Dados da Turma" no IFRS, com listas, dicionários e `Counter`. O pandas faz o mesmo tipo de coisa, mas pensado para tabelas grandes.

## Revisão rápida (SQL)

1. Escreva de cabeça um SELECT que traga as vendas PIX acima de R$ 500.
2. O que o `GROUP BY` faz?

## Analogia

- O **pandas** é um Excel que você comanda por texto.
- Um **DataFrame** é uma planilha: tem linhas, colunas e nomes de colunas.
- Uma **Series** é uma coluna sozinha.

Por que não ficar só no Excel? Porque o código é uma **receita repetível** (como o Power Query) e funciona com milhões de linhas, onde o Excel engasga. Além disso, o código mostra ao recrutador exatamente o que você fez.

Onde a analogia quebra: no pandas você não vê a tabela inteira o tempo todo. Você pede para ver pedaços (`head()`, `sample()`), e precisa confiar nos números que o código devolve.

## O que é de verdade

| Quero... | Excel | SQL | pandas |
|---|---|---|---|
| Abrir os dados | Abrir arquivo | `FROM vendas` | `pd.read_csv("vendas.csv")` |
| Ver o começo | rolar | `LIMIT 5` | `df.head()` |
| Escolher colunas | ocultar colunas | `SELECT a, b` | `df[["a", "b"]]` |
| Filtrar | Filtro | `WHERE` | `df[df["canal"] == "Loja"]` |
| Ordenar | Classificar | `ORDER BY` | `df.sort_values("valor_total")` |
| Criar coluna | nova coluna com fórmula | `AS nova` | `df["nova"] = ...` |
| Somar | `=SOMA()` | `SUM()` | `df["valor_total"].sum()` |

## Mão na massa

### Preparar o Colab

1. Entre em colab.research.google.com e crie um **Novo notebook**. Renomeie para `aula-11-pandas.ipynb`.
2. Pegue o endereço "raw" do arquivo no seu GitHub: abra `dados/vendas.csv` no site do GitHub, clique em **Raw** e copie o endereço da barra (começa com `https://raw.githubusercontent.com/...`).
3. Numa célula, escreva e rode com **Shift+Enter**:

```python
import pandas as pd

URL = "https://raw.githubusercontent.com/SEU-USUARIO/analise-de-dados/main/dados/vendas.csv"
vendas = pd.read_csv(URL, parse_dates=["data"])
```

- `import pandas as pd`: carrega a biblioteca e dá o apelido `pd`.
- `parse_dates=["data"]`: avisa que a coluna `data` é data, não texto.

### Eu faço: conhecer a tabela

```python
vendas.head()            # as 5 primeiras linhas
vendas.info()            # colunas, tipos e quantos valores preenchidos
vendas["valor_total"].describe()   # resumo estatístico
```

No `info()`, repare que `bandeira` tem menos valores preenchidos que as outras. Por quê? (Pense em PIX e dinheiro.)

No `describe()`, você reconhece média, mediana (50%), Q1 (25%) e Q3 (75%) da Aula 05.

### Fazemos juntos: filtrar e ordenar

Vendas por **PIX acima de R$ 500**, da maior para a menor:

```python
pix_grandes = vendas[(vendas["forma_pagamento"] == "____") & (vendas["valor_total"] > ___)]
pix_grandes.sort_values("valor_total", ascending=______).head(10)
```

- Cada condição fica entre parênteses.
- `&` significa E; `|` significa OU.
- `ascending=False` ordena do maior para o menor.

Quantas são? Use `len(pix_grandes)`.

### Você faz

1. Crie as colunas `ano` e `mes` com `vendas["data"].dt.year` e `vendas["data"].dt.month`.
2. Filtre 2025 e calcule faturamento, ticket médio e mediana. Os números devem bater com as Aulas 05 e 08.
3. Conte quantas vendas houve por canal em 2025 com `value_counts()`.
4. Conte quantas vendas estão sem bandeira com `.isna().sum()`.

## Checagem

1. Por que usar `parse_dates`? O que daria errado com a data como texto?
2. Qual a diferença entre `vendas["canal"]` e `vendas[["canal"]]`?
3. Traduza para pandas: `SELECT * FROM vendas WHERE canal = 'Online' ORDER BY valor_total DESC LIMIT 5;`

## No seu portfólio

No Colab: `Arquivo > Salvar uma cópia no GitHub`, escolha o seu repositório e o caminho `modulos/04-python-pandas/meus-notebooks/aula-11-pandas.ipynb`. O GitHub mostra o notebook com os resultados.

Próximo passo: Aula 12, agrupar e juntar tabelas no pandas.
