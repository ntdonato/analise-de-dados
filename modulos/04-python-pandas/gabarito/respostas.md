# Gabarito: Módulo 4 (Python e pandas)

Os scripts completos estão em `aula-11.py`, `aula-12.py`, `aula-13.py` e `projeto-2-conciliacao.py`. Para rodar no seu computador, abra a pasta do curso no terminal e rode `python modulos/04-python-pandas/gabarito/aula-11.py`. No Colab, troque o caminho `dados/...` pelo link raw do GitHub.

## Aula 11
- `bandeira` tem menos valores porque PIX, dinheiro e "lançado no quarto" não têm bandeira de cartão (10.382 vendas sem bandeira).
- Fazemos juntos: `"PIX"`, `500`, `ascending=False`. São 40 vendas; a maior é de R$ 714,00.
- 2025: faturamento R$ 1.309.451,42 · ticket médio R$ 100,50 · mediana R$ 69,90.
- Vendas por canal em 2025: Loja 10.165 · Recepção 1.784 · Online 1.081.

Checagem
1. Como texto, "2025-10-01" e "2025-9-30" não se ordenam direito e não dá para extrair mês ou dia da semana. Como data, `.dt.month` e comparações funcionam.
2. Um colchete devolve uma Series (uma coluna solta); dois colchetes devolvem um DataFrame com uma coluna.
3. `vendas[vendas["canal"] == "Online"].sort_values("valor_total", ascending=False).head(5)`

## Aula 12
- Fazemos juntos: `on="ano_mes"`, `painel["meta"]`, `x >= 100`.
- Margem por categoria: igual à Aula 09 (Cafeteria 68,1% · Bebidas 54,8%).
- Canal × dia: o pico da Loja é no domingo; o do Online e o da Recepção é na sexta.

Checagem
1. Transforma o rótulo do grupo (que virou índice) de volta numa coluna comum, para poder fazer merge, filtrar e exportar.
2. `inner` mantém só o que casa nas duas tabelas; `left` mantém tudo da esquerda, com NaN onde não houver par.
3. Não é erro: cada venda tem um ou mais itens, então ela se repete uma vez por item. Só não some `valor_total` depois disso.

## Aula 13
- Fazemos juntos: `aggfunc="count"`. O título precisa mudar ("Número de vendas mensal..."), senão fica mentindo.

Checagem
1. Para guiar o olho para o foco (o ano atual). O ano anterior é só contexto.
2. A barra mostra tamanho pelo comprimento: cortar o eixo exagera diferenças. A linha mostra variação e tendência, então dá para ajustar a escala, deixando isso claro.
3. Exemplo: "A Loja traz 78% do faturamento; o Online ainda é 8%".

## Projeto 2 (conciliação)

| Status | Qtd | Diferença |
|---|---|---|
| OK | 20.652 | R$ 0,00 |
| Não recebido | 270 | R$ 27.338,16 |
| Valor a menor | 195 | R$ 124,54 |
| Atraso | 169 | R$ 0,00 (atraso médio de 5,8 dias) |

Dinheiro a cobrar das operadoras: **R$ 27.462,70**. Não recebidos por operadora: Stone R$ 12.357,64 · Vero R$ 8.090,14 · PIX R$ 6.890,38.
