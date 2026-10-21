# Projeto 2: Conciliação de recebíveis de maquininhas com Python

> **Status:** a fazer. Depois de concluir, troque esta linha pelo resultado principal (ex.: "Encontrei R$ X em repasses não pagos").

## Contexto
Toda venda no cartão ou PIX gera um **recebível**: o dinheiro que a operadora (Stone, Vero) deve depositar, descontada a taxa contratada, numa data prevista. Na prática, alguns repasses não chegam, chegam com valor menor ou atrasam. Conferir isso à mão, venda por venda, é inviável.

Este projeto automatiza a conciliação de cerca de 21 mil transações de 2024 e 2025 do Empório Serra Alta (loja fictícia).

## Perguntas
1. Quantas transações estão OK, não recebidas, pagas a menor ou atrasadas?
2. Quanto dinheiro deixou de entrar? Em qual operadora?
3. Qual o atraso médio dos repasses atrasados?
4. Gerar uma lista de pendências para cobrar das operadoras.

## Ferramentas
Python · pandas · matplotlib · Google Colab

## Como reproduzir
Abra `conciliacao.ipynb` no Google Colab (link abaixo) e execute todas as células. Os dados são lidos de `dados/recebiveis.csv` neste repositório.

## Método
1. Ler `recebiveis.csv` com as datas convertidas.
2. Classificar cada transação: **Não recebido** (sem valor recebido), **Valor a menor** (recebido < líquido esperado), **Atraso** (data recebida > data prevista), **OK**.
3. Calcular a diferença em R$ e os dias de atraso.
4. Resumir por status e por operadora; gerar gráfico e exportar `pendencias_conciliacao.csv`.

## Resultados
(tabela-resumo + gráfico + 3 frases de conclusão)

## O que aprendi
(2 a 3 linhas)

---
### Checklist antes de publicar
- [ ] Notebook `conciliacao.ipynb` executado, com as saídas visíveis
- [ ] Células de texto explicando cada etapa (não só código)
- [ ] Um gráfico salvo como `.png` e exibido aqui no README
- [ ] `pendencias_conciliacao.csv` gerado
- [ ] Link "Abrir no Colab" no topo do README
