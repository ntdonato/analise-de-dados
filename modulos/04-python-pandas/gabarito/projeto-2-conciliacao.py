# Gabarito do Projeto 2: conciliação de recebíveis
import pandas as pd

rec = pd.read_csv("dados/recebiveis.csv", parse_dates=["data_venda", "data_prevista", "data_recebida"])

def classifica(l):
    if pd.isna(l["valor_recebido"]):
        return "Não recebido"
    if round(l["valor_recebido"], 2) < round(l["valor_liquido_esperado"], 2):
        return "Valor a menor"
    if l["data_recebida"] > l["data_prevista"]:
        return "Atraso"
    return "OK"

rec["status"] = rec.apply(classifica, axis=1)
rec["diferenca"] = (rec["valor_liquido_esperado"] - rec["valor_recebido"].fillna(0)).round(2)
rec["dias_atraso"] = (rec["data_recebida"] - rec["data_prevista"]).dt.days

resumo = rec.groupby("status").agg(qtd=("id_venda", "count"), diferenca=("diferenca", "sum")).round(2)
print(resumo)
por_maq = rec[rec["status"] != "OK"].pivot_table(index="maquininha", columns="status",
                                                 values="diferenca", aggfunc="sum", fill_value=0).round(2)
print(por_maq)
print("Dinheiro a cobrar:", round(rec.loc[rec["status"].isin(["Não recebido", "Valor a menor"]), "diferenca"].sum(), 2))
print("Atraso médio (dias):", round(rec.loc[rec["status"] == "Atraso", "dias_atraso"].mean(), 1))
rec[rec["status"] != "OK"].to_csv("pendencias_conciliacao.csv", index=False)
