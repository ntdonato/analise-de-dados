# Aula 12: groupby, merge e datas
import pandas as pd

vendas = pd.read_csv("dados/vendas.csv", parse_dates=["data"])
itens = pd.read_csv("dados/itens_venda.csv")
produtos = pd.read_csv("dados/produtos.csv")
metas = pd.read_csv("dados/metas_mensais.csv")

# Eu faço: faturamento por mês
vendas["ano_mes"] = vendas["data"].dt.strftime("%Y-%m")
por_mes = vendas.groupby("ano_mes").agg(n_vendas=("id_venda", "count"),
                                        faturamento=("valor_total", "sum")).reset_index()
print(por_mes.tail(12))

# Fazemos juntos: meta x realizado com merge
painel = por_mes.merge(metas, on="ano_mes", how="left")
painel["pct_meta"] = (painel["faturamento"] / painel["meta"] * 100).round(1)
painel["situacao"] = painel["pct_meta"].apply(lambda x: "Bateu" if x >= 100 else "Não bateu")
print(painel[painel["ano_mes"].str.startswith("2025")])

# Você faz 1: faturamento e margem por categoria em 2025
base = (itens.merge(produtos, on="id_produto")
             .merge(vendas[["id_venda", "data"]], on="id_venda"))
base = base[base["data"].dt.year == 2025]
base["custo"] = base["quantidade"] * base["custo_unitario"]
cat = base.groupby("categoria").agg(receita=("valor_item", "sum"), custo=("custo", "sum"))
cat["margem_pct"] = ((cat["receita"] - cat["custo"]) / cat["receita"] * 100).round(1)
print(cat.sort_values("receita", ascending=False).round(2))

# Você faz 2: tabela canal x dia da semana (pivot_table)
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
vendas["dia_semana"] = vendas["data"].dt.dayofweek.map(dict(enumerate(dias)))
v25 = vendas[vendas["data"].dt.year == 2025]
tabela = v25.pivot_table(index="canal", columns="dia_semana", values="valor_total",
                         aggfunc="sum").reindex(columns=dias).round(0)
print(tabela)
