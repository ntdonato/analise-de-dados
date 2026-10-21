# Aula 05: Média, mediana, desvio padrão e outliers

**Objetivo:** descrever as vendas de 2025 com 5 números e explicar ao gerente por que "o ticket médio é R$ 100" engana.

**Tempo:** cerca de 3 horas. **Arquivo:** o `aula-03-metas.xlsx` da Aula 03 (Tabela `tbVendas`).

## Analogia

Imagine 10 hóspedes no café da manhã. Nove gastam R$ 20 e um compra um kit presente de R$ 250.

- **Média:** (9 × 20 + 250) ÷ 10 = R$ 43. Ninguém gastou R$ 43!
- **Mediana:** coloque os 10 valores em fila, do menor ao maior, e pegue o do meio: R$ 20. Isso representa o hóspede típico.

O hóspede do kit puxou a média para cima. Ele é um **outlier** (valor muito fora do padrão).

Onde a analogia quebra: outlier não é erro. Às vezes o outlier é justamente o cliente mais valioso. A estatística aponta; quem decide se é erro ou oportunidade é você.

## O que é de verdade

| Medida | Responde | Excel |
|---|---|---|
| Média | Valor "por cabeça" se tudo fosse dividido igual | `=MÉDIA()` |
| Mediana | Valor do meio; metade está abaixo | `=MED()` |
| Desvio padrão | Quanto os valores se espalham em volta da média | `=DESVPAD.A()` |
| Quartis (Q1, Q3) | Onde ficam 25% e 75% dos valores | `=QUARTIL.INC(;1)` e `;3` |
| Amplitude interquartil (IQR) | Q3 − Q1, o "miolo" dos dados | conta simples |

Regra prática de outlier (regra de Tukey): é outlier quem está acima de **Q3 + 1,5 × IQR** ou abaixo de **Q1 − 1,5 × IQR**.

Quando média e mediana são muito diferentes, os dados são **assimétricos** (tem uma "cauda" de valores altos). Nesse caso, reporte a mediana junto com a média.

```
menor ──[Q1]────[mediana]────[Q3]──────────────── maior
              |←── IQR ──→|          outliers →  • •  •
```

## Mão na massa

Crie uma aba `Estatística` e filtre só 2025. Dica: use `FILTRO` para separar os valores de 2025 numa coluna auxiliar:

```
=FILTRO(tbVendas[valor_total]; ANO(tbVendas[data])=2025)
```

### Eu faço

Monte este quadro, apontando para a coluna filtrada (ex.: `A2#`, o `#` pega todo o resultado do FILTRO):

| Medida | Fórmula |
|---|---|
| Nº de vendas | `=CONT.NÚM(A2#)` |
| Média | `=MÉDIA(A2#)` |
| Mediana | `=MED(A2#)` |
| Desvio padrão | `=DESVPAD.A(A2#)` |
| Mínimo / Máximo | `=MÍNIMO(A2#)` / `=MÁXIMO(A2#)` |

Leia o resultado: a média é bem maior que a mediana. A distribuição tem cauda para a direita (algumas vendas grandes, de kits e cestas).

### Fazemos juntos: quartis e outliers

Complete:

```
Q1          =QUARTIL.INC(A2#; ___)
Q3          =QUARTIL.INC(A2#; ___)
IQR         = Q3 − ____
Limite sup. = Q3 + ___ * IQR
Outliers    =CONT.SE(A2#; ">"&[limite superior])
```

### Você faz

1. Faça um **histograma** (`Inserir > Gráfico Estatístico > Histograma`) dos valores de 2025. Descreva o formato em uma frase.
2. Calcule média e mediana por canal (Loja, Recepção, Online). O canal muda o ticket?
3. Escreva um parágrafo de 3 linhas para o gerente: "Como é a venda típica da loja?". Use mediana, Q1 e Q3.

## Checagem

1. Por que a mediana representa melhor a "venda típica" desta loja do que a média?
2. Um colega quer apagar os outliers da base "porque atrapalham a média". O que você responde?
3. Se o desvio padrão fosse zero, o que isso diria sobre as vendas?

## No seu portfólio

Salve `modulos/02-estatistica/meus-arquivos/aula-05.xlsx` e o print do histograma. Commit: `Aula 05: estatística descritiva das vendas 2025`.

Próximo passo: Aula 06, variação e correlação.
