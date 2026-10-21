# Projeto 5: Fechamento de caixa automatizado com VBA

> **Status:** a fazer. Depois de concluir, troque por um GIF ou print da macro funcionando.

## Contexto
Na recepção e na loja de um hotel, o fechamento de caixa é feito todo dia, à mão: somar o sistema por forma de pagamento, comparar com o que foi contado e anotar as diferenças. Este projeto faz isso com um clique.

## O que as macros fazem
| Botão | Macro | Faz |
|---|---|---|
| Fechar caixa | `FecharCaixa` | Soma o sistema por forma de pagamento na data escolhida, compara com o contado e marca OK ou divergência |
| Resumo do mês | `ResumoDoMes` | Cria uma aba com uma linha por dia e uma coluna por forma de pagamento |
| Gerar PDF | `ExportarFechamentoPDF` | Salva o fechamento em PDF com a data no nome |

## Ferramentas
Excel · VBA

## Arquivos
- `fechamento-caixa-modelo.xlsx`: planilha de partida (sem macros)
- `fechamento-caixa.xlsm`: sua versão com macros
- `FechamentoCaixa.bas`: o código, em texto, para ler aqui no GitHub

---
### Checklist antes de publicar
- [ ] `.xlsm` funcionando com os 3 botões
- [ ] Código exportado como `.bas`, com comentários
- [ ] Print ou GIF (ex.: com ScreenToGif) mostrando o fechamento
