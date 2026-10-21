# Aula 11: primeiros passos com pandas
import pandas as pd

URL = "dados/vendas.csv"  # no Colab: troque pelo link "raw" do seu GitHub
vendas = pd.read_csv(URL, parse_dates=["data"])

# Eu faço
print(vendas.head())
vendas.info()
print(vendas["valor_total"].describe())

# Fazemos juntos: só PIX acima de R$ 500, do maior para o menor
pix_grandes = vendas[(vendas["forma_pagamento"] == "PIX") & (vendas["valor_total"] > 500)]
print(pix_grandes.sort_values("valor_total", ascending=False).head(10))
print("Qtd:", len(pix_grandes))

# Você faz
vendas["ano"] = vendas["data"].dt.year
vendas["mes"] = vendas["data"].dt.month
v2025 = vendas[vendas["ano"] == 2025]
print("Faturamento 2025:", round(v2025["valor_total"].sum(), 2))
print("Ticket médio 2025:", round(v2025["valor_total"].mean(), 2))
print("Mediana 2025:", round(v2025["valor_total"].median(), 2))
print(v2025["canal"].value_counts())
print("Vendas sem bandeira:", vendas["bandeira"].isna().sum())
