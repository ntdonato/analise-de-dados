# Aula 12: groupby, merge e datas

**Objetivo:** refazer em pandas o painel de metas e a margem por categoria, juntando várias tabelas.

**Tempo:** cerca de 3 horas.

## Revisão rápida

1. Como filtrar 2025 no pandas?
2. Traduza para SQL: `vendas["valor_total"].mean()`.

## Analogia

Você já sabe a lógica. Só muda a palavra:

| Ideia | Excel | SQL | pandas |
|---|---|---|---|
| Separar em montinhos e somar | Tabela dinâmica | `GROUP BY` | `df.groupby("col").agg(...)` |
| Cruzar duas tabelas | PROCX | `JOIN` | `df.merge(outra, on="chave")` |
| Linhas × colunas | Tabela dinâmica com Colunas | (complicado) | `df.pivot_table(...)` |

Onde a analogia quebra: o `groupby` devolve o nome do grupo como **índice** (o "rótulo" das linhas), não como coluna. Por isso quase sempre se usa `.reset_index()` no fim, para ele voltar a ser uma coluna normal.

## O que é de verdade

```python
df.groupby("coluna").agg(
    nome_resultado=("coluna_origem", "funcao"),   # sum, mean, count, median, min, max
)
```

```python
a.merge(b, on="chave", how="left")   # how: "inner" (JOIN) ou "left" (LEFT JOIN)
```

Datas: `df["data"].dt.year`, `.dt.month`, `.dt.dayofweek` (0 = segunda), `.dt.strftime("%Y-%m")` (vira texto "2025-07").

## Mão na massa

Carregue `vendas`, `itens_venda`, `produtos` e `metas_mensais` do seu GitHub, como na Aula 11.

### Eu faço: faturamento por mês

```python
vendas["ano_mes"] = vendas["data"].dt.strftime("%Y-%m")

por_mes = (vendas.groupby("ano_mes")
                 .agg(n_vendas=("id_venda", "count"),
                      faturamento=("valor_total", "sum"))
                 .reset_index())
por_mes.tail(12)
```

Os parênteses em volta permitem quebrar o código em várias linhas, uma etapa por linha. Fica mais fácil de ler.

### Fazemos juntos: meta × realizado

```python
painel = por_mes.merge(metas, on="________", how="left")
painel["pct_meta"] = (painel["faturamento"] / painel["____"] * 100).round(1)
painel["situacao"] = painel["pct_meta"].apply(lambda x: "Bateu" if x >= ___ else "Não bateu")
painel[painel["ano_mes"].str.startswith("2025")]
```

`lambda x: ...` é uma mini função de uma linha: "para cada valor x, devolva...". É o `SE` do Excel aplicado à coluna inteira.

O resultado deve ser igual ao da Aula 03 (Excel) e da Aula 10 (SQL). Três ferramentas, mesmo número.

### Você faz

1. **Margem por categoria em 2025:** junte `itens_venda` com `produtos` (pela chave `id_produto`) e com `vendas` (pela chave `id_venda`, só as colunas `id_venda` e `data`). Crie a coluna `custo = quantidade × custo_unitario`, agrupe por categoria e calcule receita, custo e margem %.
2. **Canal × dia da semana em 2025** com `pivot_table`: canais nas linhas, dias da semana nas colunas, soma do faturamento nos valores. Dica para os nomes dos dias:
   ```python
   dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
   vendas["dia_semana"] = vendas["data"].dt.dayofweek.map(dict(enumerate(dias)))
   ```

## Checagem

1. Para que serve o `.reset_index()` depois do `groupby`?
2. No `merge`, o que muda entre `how="inner"` e `how="left"`?
3. Você juntou itens com vendas e o número de linhas aumentou. Isso é erro? Por quê?

## No seu portfólio

Salve no GitHub como `meus-notebooks/aula-12-groupby-merge.ipynb`.

Próximo passo: Aula 13, gráficos que contam uma história.
