# Aula 13: gráficos com matplotlib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

vendas = pd.read_csv("dados/vendas.csv", parse_dates=["data"])
vendas["ano"] = vendas["data"].dt.year
vendas["mes"] = vendas["data"].dt.month

# Eu faço: linha 2024 x 2025
mensal = vendas.pivot_table(index="mes", columns="ano", values="valor_total", aggfunc="sum")
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(mensal.index, mensal[2024] / 1000, marker="o", color="#9aa5a3", label="2024")
ax.plot(mensal.index, mensal[2025] / 1000, marker="o", color="#0d6b66", linewidth=2.5, label="2025")
ax.set_title("Faturamento mensal (R$ mil): julho e dezembro são os picos")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"])
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("faturamento_mensal.png", dpi=150)

# Você faz: barras horizontais de faturamento por categoria em 2025
itens = pd.read_csv("dados/itens_venda.csv")
produtos = pd.read_csv("dados/produtos.csv")
base = itens.merge(produtos, on="id_produto").merge(vendas[["id_venda", "ano"]], on="id_venda")
cat = base[base["ano"] == 2025].groupby("categoria")["valor_item"].sum().sort_values()
fig, ax = plt.subplots(figsize=(8, 4))
cores = ["#0d6b66" if c == cat.idxmax() else "#b9c6c4" for c in cat.index]
ax.barh(cat.index, cat.values / 1000, color=cores)
for i, val in enumerate(cat.values / 1000):
    ax.text(val + 3, i, f"{val:,.0f} mil".replace(",", "."), va="center")
ax.set_title("Kits Presente lideram o faturamento de 2025 (R$ mil)")
ax.spines[["top", "right", "bottom"]].set_visible(False)
ax.set_xticks([])
fig.tight_layout()
fig.savefig("faturamento_categoria.png", dpi=150)
print("gráficos salvos")
