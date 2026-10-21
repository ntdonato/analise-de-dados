# Aula 13: Gráficos com matplotlib

**Objetivo:** fazer dois gráficos limpos, prontos para um relatório, e salvá-los como imagem no portfólio.

**Tempo:** cerca de 2h30.

## Revisão rápida

1. Escreva o `groupby` que dá o faturamento por canal.
2. Qual a diferença entre `merge` e `concat`? (Se não souber o `concat`, pesquise: é empilhar tabelas uma embaixo da outra.)

## Analogia

Um gráfico é um **recado para o gerente** que ele entende em 5 segundos. O título é a frase do recado; o gráfico é a prova.

Gráfico ruim: título "Faturamento", 7 cores, grade forte, legenda longe.
Gráfico bom: título "Dezembro foi o melhor mês dos dois anos", uma cor de destaque, o resto em cinza.

Onde a analogia quebra: um recado pode ter opinião. O gráfico precisa ser honesto: eixo de barras começando no zero e escala igual para comparar coisas iguais.

## O que é de verdade

**matplotlib** é a biblioteca de gráficos mais usada em Python. A estrutura básica:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 4))   # fig = a folha; ax = a área do gráfico
ax.plot(x, y)                            # linha
ax.bar(x, y)  /  ax.barh(nomes, valores) # barras verticais / horizontais
ax.set_title("Frase com a conclusão")
fig.savefig("grafico.png", dpi=150)
```

Qual gráfico usar:

| Quero mostrar | Gráfico |
|---|---|
| Evolução no tempo | Linha |
| Comparar categorias | Barras (horizontais se os nomes forem longos) |
| Parte de um todo | Barras empilhadas ou 100%. Pizza só com 2 ou 3 fatias |
| Relação entre duas medidas | Dispersão |

## Mão na massa

### Eu faço: 2024 × 2025 mês a mês

```python
import matplotlib.pyplot as plt

vendas["ano"] = vendas["data"].dt.year
vendas["mes"] = vendas["data"].dt.month
mensal = vendas.pivot_table(index="mes", columns="ano", values="valor_total", aggfunc="sum")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(mensal.index, mensal[2024] / 1000, marker="o", color="#9aa5a3", label="2024")
ax.plot(mensal.index, mensal[2025] / 1000, marker="o", color="#0d6b66", linewidth=2.5, label="2025")
ax.set_title("Faturamento mensal (R$ mil): julho e dezembro são os picos")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"])
ax.spines[["top", "right"]].set_visible(False)   # tira as bordas de cima e da direita
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("faturamento_mensal.png", dpi=150)
```

Repare nas escolhas: 2024 em cinza (contexto), 2025 em cor forte (o foco), valores em R$ mil para os números do eixo ficarem curtos.

### Fazemos juntos

Mude o gráfico acima para mostrar **número de vendas** em vez de faturamento. O que você troca no `pivot_table`? (Dica: `values="id_venda"` e `aggfunc="______"`.) O título continua verdadeiro?

### Você faz

Faça um gráfico de **barras horizontais** com o faturamento de 2025 por categoria (você calculou na Aula 12):

- ordenado do maior para o menor;
- a maior barra numa cor forte, as outras em cinza claro;
- o valor escrito na ponta de cada barra (`ax.text`);
- um título que diga a conclusão;
- salvo como `faturamento_categoria.png`.

O gabarito (`gabarito/aula-13.py`) tem uma versão pronta, mas tente antes.

## Checagem

1. Por que usar cinza para 2024 e cor forte para 2025?
2. Por que um gráfico de barras precisa começar no zero, e um de linha não necessariamente?
3. Escreva um título de gráfico que traga uma conclusão sobre os canais de venda.

## No seu portfólio

Salve o notebook e as duas imagens em `meus-notebooks/`. As imagens vão aparecer no README do Projeto 2.

Agora faça o **Projeto 2** (`projetos/p2-python-conciliacao/`).
