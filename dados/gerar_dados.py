"""Gera a base fictícia do curso: Empório Serra Alta, a loja de chocolates
de um hotel (fictício) na serra gaúcha. Todos os dados são inventados.
Rode: python gerar_dados.py  (gera os CSVs e o banco loja.db nesta pasta)"""
import csv, random, sqlite3, os
from datetime import date, timedelta, datetime

random.seed(42)
AQUI = os.path.dirname(os.path.abspath(__file__))

PRODUTOS = [
 # id, nome, categoria, preco, custo
 (1,"Barra ao leite 100g","Chocolates",18.90,7.20),(2,"Barra meio amargo 70% 100g","Chocolates",21.90,8.40),
 (3,"Barra branca com morango 100g","Chocolates",19.90,7.80),(4,"Barra crocante 100g","Chocolates",19.90,7.50),
 (5,"Barra ao leite 300g","Chocolates",44.90,17.00),(6,"Tablete zero açúcar 80g","Chocolates",24.90,10.10),
 (7,"Trufa tradicional","Trufas",6.50,2.10),(8,"Trufa de maracujá","Trufas",6.90,2.30),
 (9,"Trufa de licor","Trufas",7.90,2.80),(10,"Caixa 6 trufas sortidas","Trufas",39.90,13.50),
 (11,"Caixa 12 trufas sortidas","Trufas",74.90,25.00),(12,"Bombom recheado unidade","Trufas",4.90,1.60),
 (13,"Kit presente pequeno","Kits Presente",89.90,36.00),(14,"Kit presente médio","Kits Presente",149.90,58.00),
 (15,"Kit presente grande","Kits Presente",249.90,97.00),(16,"Cesta café colonial","Kits Presente",219.90,92.00),
 (17,"Ovo de Páscoa 250g","Sazonais",69.90,26.00),(18,"Panetone trufado 500g","Sazonais",79.90,31.00),
 (19,"Fondue kit 2 pessoas","Kits Presente",129.90,52.00),(20,"Chocolate quente cremoso (copo)","Cafeteria",16.00,4.80),
 (21,"Cappuccino","Cafeteria",14.00,3.90),(22,"Café expresso","Cafeteria",8.00,1.90),
 (23,"Fatia de torta","Cafeteria",22.00,8.50),(24,"Licor de chocolate 500ml","Bebidas",64.90,27.00),
 (25,"Vinho espumante moscatel","Bebidas",79.90,38.00),(26,"Caneca personalizada","Souvenirs",39.90,14.00),
 (27,"Ímã de geladeira","Souvenirs",15.90,4.20),(28,"Pelúcia mascote","Souvenirs",59.90,22.00),
 (29,"Pirulito de chocolate","Chocolates",9.90,3.10),(30,"Drágeas sortidas 150g","Chocolates",29.90,11.00),
]
PESO_CAT = {"Chocolates":30,"Trufas":28,"Kits Presente":9,"Sazonais":0,"Cafeteria":22,"Bebidas":4,"Souvenirs":7}
SAZ_MES = {1:1.15,2:0.80,3:0.85,4:0.95,5:0.80,6:1.10,7:1.55,8:1.05,9:0.95,10:1.00,11:1.20,12:1.60}
FORMAS = [("Crédito",44),("Débito",20),("PIX",24),("Dinheiro",5),("Lançado no quarto",7)]
BANDEIRAS = [("Visa",45),("Mastercard",38),("Elo",17)]
TAXAS = {("Stone","Crédito"):(3.19,30),("Stone","Débito"):(1.29,1),("Vero","Crédito"):(3.49,30),("Vero","Débito"):(1.39,1),("PIX","PIX"):(0.0,0)}

def escolhe(pares):
    return random.choices([p[0] for p in pares],[p[1] for p in pares])[0]

def produtos_do_dia(d):
    pesos=[]
    for p in PRODUTOS:
        w = PESO_CAT[p[2]]/sum(1 for q in PRODUTOS if q[2]==p[2])
        if p[0]==17: w = 25 if (d.month==3 or (d.month==4 and d.day<=20)) else 0
        if p[0]==18: w = 18 if d.month in (11,12) else 0
        if p[0]==19: w *= 2.2 if d.month in (6,7,8) else 1
        if p[0]==20: w *= 2.5 if d.month in (6,7,8) else 0.6
        pesos.append(w)
    return pesos

vendas=[]; itens=[]; recebiveis=[]
vid=0
d=date(2024,1,1)
while d<=date(2025,12,31):
    base = 26*SAZ_MES[d.month]*(1.45 if d.weekday()>=4 else 1.0)*(1.08 if d.year==2025 else 1.0)
    n = max(3,int(random.gauss(base, base*0.22)))
    pesos=produtos_do_dia(d)
    for _ in range(n):
        vid+=1
        hora = f"{random.choices(range(9,23),[2,4,6,8,9,9,10,11,11,10,9,7,5,3])[0]:02d}:{random.randint(0,59):02d}"
        canal = random.choices(["Loja","Recepção","Online"],[78,14,8])[0]
        forma = escolhe(FORMAS)
        if canal=="Online": forma = random.choice(["Crédito","PIX"])
        if canal=="Recepção" and random.random()<0.4: forma="Lançado no quarto"
        band = escolhe(BANDEIRAS) if forma in ("Crédito","Débito") else ""
        maq = random.choices(["Stone","Vero"],[65,35])[0] if forma in ("Crédito","Débito") else ("PIX" if forma=="PIX" else "")
        total=0
        for _ in range(random.choices([1,2,3,4],[50,30,14,6])[0]):
            p = random.choices(PRODUTOS,pesos)[0]
            q = random.choices([1,2,3,4,6],[60,22,9,5,4])[0]
            if p[2] in ("Kits Presente","Bebidas"): q=1
            desconto = 0.10 if random.random()<0.06 else 0.0
            valor = round(p[3]*q*(1-desconto),2)
            itens.append((vid,p[0],q,p[3],desconto,valor)); total+=valor
        total=round(total,2)
        vendas.append((vid,d.isoformat(),hora,canal,forma,band,maq,total))
        if maq in ("Stone","Vero","PIX"):
            fx = "PIX" if maq=="PIX" else forma
            taxa,prazo = TAXAS[(maq,fx)]
            liq = round(total*(1-taxa/100),2)
            prev = d+timedelta(days=prazo)
            receb_data, receb_val = prev.isoformat(), liq
            r=random.random()
            if r<0.012: receb_data, receb_val = "", None            # não recebido
            elif r<0.022: receb_val = round(total*(1-(taxa+0.6)/100),2) # taxa cobrada a maior
            elif r<0.030: receb_data = (prev+timedelta(days=random.randint(2,9))).isoformat()  # atraso
            recebiveis.append((vid,maq,forma if maq!="PIX" else "PIX",d.isoformat(),prev.isoformat(),total,taxa,liq,receb_data,receb_val))
    d+=timedelta(days=1)

# metas mensais (redondas, como num controle real)
from collections import defaultdict
real=defaultdict(float)
for v in vendas: real[v[1][:7]]+=v[7]
metas=[]
for am in sorted(real):
    alvo = real[am]*random.uniform(0.92,1.12)
    metas.append((am, int(round(alvo/5000.0))*5000))

def salva(nome,cab,linhas):
    with open(os.path.join(AQUI,nome),"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(cab); w.writerows(linhas)

salva("produtos.csv",["id_produto","produto","categoria","preco_unitario","custo_unitario"],PRODUTOS)
salva("vendas.csv",["id_venda","data","hora","canal","forma_pagamento","bandeira","maquininha","valor_total"],vendas)
salva("itens_venda.csv",["id_venda","id_produto","quantidade","preco_unitario","desconto_pct","valor_item"],itens)
salva("metas_mensais.csv",["ano_mes","meta"],metas)
salva("taxas_maquininha.csv",["maquininha","forma_pagamento","taxa_percentual","prazo_dias"],[(k[0],k[1],v[0],v[1]) for k,v in TAXAS.items()])
salva("recebiveis.csv",["id_venda","maquininha","forma_pagamento","data_venda","data_prevista","valor_bruto","taxa_percentual","valor_liquido_esperado","data_recebida","valor_recebido"],recebiveis)

# arquivo "sujo" para a aula de Power Query: export de PDV de dezembro/2025 do jeito que sistemas exportam
suja=[]
for v in [x for x in vendas if x[1].startswith("2025-12")]:
    dt=datetime.fromisoformat(v[1]).strftime("%d/%m/%Y")
    val=f"R$ {v[7]:,.2f}".replace(",","X").replace(".",",").replace("X",".")
    forma=v[4]
    if random.random()<0.15: forma=forma.upper()
    if random.random()<0.10: forma="  "+forma+" "
    suja.append([dt,v[2],forma,v[5] or "-",val,f"PDV-{v[0]}"])
for _ in range(12): suja.insert(random.randint(0,len(suja)),list(random.choice(suja)))  # duplicadas
suja.insert(0,["RELATÓRIO DE VENDAS - EMPÓRIO SERRA ALTA","","","","",""])
suja.insert(1,["Período: 01/12/2025 a 31/12/2025","","","","",""])
suja.insert(2,["","","","","",""])
with open(os.path.join(AQUI,"export_pdv_dez2025.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f,delimiter=";")
    w.writerows(suja[:3]); w.writerow(["Data","Hora","Forma Pgto","Bandeira","Valor","Documento"]); w.writerows(suja[3:])

# banco SQLite
db=os.path.join(AQUI,"loja.db")
if os.path.exists(db): os.remove(db)
con=sqlite3.connect(db); c=con.cursor()
c.executescript("""
CREATE TABLE produtos(id_produto INTEGER PRIMARY KEY, produto TEXT, categoria TEXT, preco_unitario REAL, custo_unitario REAL);
CREATE TABLE vendas(id_venda INTEGER PRIMARY KEY, data TEXT, hora TEXT, canal TEXT, forma_pagamento TEXT, bandeira TEXT, maquininha TEXT, valor_total REAL);
CREATE TABLE itens_venda(id_venda INTEGER REFERENCES vendas(id_venda), id_produto INTEGER REFERENCES produtos(id_produto), quantidade INTEGER, preco_unitario REAL, desconto_pct REAL, valor_item REAL);
CREATE TABLE metas_mensais(ano_mes TEXT PRIMARY KEY, meta REAL);
CREATE TABLE taxas_maquininha(maquininha TEXT, forma_pagamento TEXT, taxa_percentual REAL, prazo_dias INTEGER);
CREATE TABLE recebiveis(id_venda INTEGER REFERENCES vendas(id_venda), maquininha TEXT, forma_pagamento TEXT, data_venda TEXT, data_prevista TEXT, valor_bruto REAL, taxa_percentual REAL, valor_liquido_esperado REAL, data_recebida TEXT, valor_recebido REAL);
""")
c.executemany("INSERT INTO produtos VALUES(?,?,?,?,?)",PRODUTOS)
c.executemany("INSERT INTO vendas VALUES(?,?,?,?,?,?,?,?)",[tuple(x if x!="" else None for x in v) for v in vendas])
c.executemany("INSERT INTO itens_venda VALUES(?,?,?,?,?,?)",itens)
c.executemany("INSERT INTO metas_mensais VALUES(?,?)",metas)
c.executemany("INSERT INTO taxas_maquininha VALUES(?,?,?,?)",[(k[0],k[1],v[0],v[1]) for k,v in TAXAS.items()])
c.executemany("INSERT INTO recebiveis VALUES(?,?,?,?,?,?,?,?,?,?)",[tuple(x if x!="" else None for x in r) for r in recebiveis])
con.commit(); con.close()
print(f"vendas: {len(vendas)} | itens: {len(itens)} | recebíveis: {len(recebiveis)} | meses: {len(metas)}")
