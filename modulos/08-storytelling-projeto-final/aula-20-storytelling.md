# Aula 20: Storytelling com dados

**Objetivo:** transformar os números de 2025 numa recomendação de uma página que o gerente lê em 2 minutos e sabe o que fazer.

**Tempo:** cerca de 3 horas.

## Revisão rápida

1. Em quantos meses de 2025 a loja bateu a meta?
2. Quanto a loja cresceu em 2025 contra 2024?

## Analogia

Pense na passagem de turno da recepção. Você não lê para o colega o livro de ocorrências inteiro. Você diz:

> "O 204 reclamou do chuveiro (**situação**). A manutenção só chega amanhã (**complicação**). Ofereci trocar para o 210 se ele pedir de novo (**resolução**)."

Em 15 segundos o colega sabe o que aconteceu e o que fazer. Storytelling com dados é a passagem de turno do analista.

Onde a analogia quebra: na passagem de turno, ninguém pede prova. Num relatório, cada frase importante precisa de um número ou de um gráfico que a sustente.

## O que é de verdade

### Estrutura SCR
| Parte | Pergunta | Tamanho |
|---|---|---|
| **S**ituação | O que todos já sabem? | 1–2 frases |
| **C**omplicação | O que mudou ou o que está errado? | 1–2 frases com número |
| **R**esolução | O que recomendo fazer? | 1–3 ações concretas |

### Pirâmide: comece pela conclusão
Gerentes leem o começo e param. Coloque a recomendação **no topo**. Os detalhes e a metodologia vão no fim, para quem quiser conferir.

### Checklist de um bom gráfico de relatório (Aula 13)
- Título é uma frase com a conclusão.
- Uma cor de destaque; o resto em cinza.
- Sem legenda se der para escrever o nome direto na linha ou barra.
- Fonte dos dados escrita embaixo.

## Mão na massa

### Eu faço: uma conclusão bem escrita

Ruim:
> "O faturamento de dezembro/2025 foi R$ 202.382,25 e a meta era R$ 215.000,00, atingindo 94,1%."

Bom:
> "Dezembro cresceu 11% sobre 2024, o melhor resultado do ano, mas ficou 6% abaixo da meta. A meta pedia um salto de 18%, três vezes o crescimento médio da loja."

O segundo dá o número, o contexto (comparação) e a explicação. O gerente entende que o problema talvez esteja na meta, não na loja.

### Fazemos juntos: investigar a complicação

Use a ferramenta que preferir (SQL, pandas ou Power BI):

1. Calcule, para cada mês de 2025, quanto a meta pedia de crescimento sobre o **realizado** do mesmo mês de 2024: `meta_2025 ÷ realizado_2024 − 1`.
2. Coloque lado a lado com o crescimento que de fato aconteceu (Aula 06).
3. Pergunta: os meses que não bateram a meta são os que tinham metas mais "puxadas"? Complete a frase: "Nos meses em que a meta pedia mais de ___% de crescimento, a loja ______."

### Você faz: o relatório de uma página

Escreva `projetos/projeto-final/relatorio-2025.md` com:

1. **Título-conclusão** (uma frase).
2. **SCR** em 5 a 7 linhas.
3. **Dois gráficos** (pode reaproveitar os do Projeto 2 ou do Power BI), cada um com título-conclusão.
4. **Três recomendações** concretas e mensuráveis. Exemplo de formato: "Definir as metas de 2026 como realizado de 2025 + X%, ajustado por sazonalidade".
5. **Como foi feito** (2 linhas): fonte dos dados e ferramentas.

Depois leia em voz alta, cronometrando. Passou de 2 minutos? Corte.

## Checagem

1. Por que a recomendação vai no começo e não no fim?
2. Reescreva no formato "bom": "O canal Online faturou R$ 106.129,56 em 2025."
3. Que pergunta o gerente provavelmente fará depois de ler o seu relatório? Você tem a resposta?

## No seu portfólio

`projetos/projeto-final/relatorio-2025.md`. Commit: `Aula 20: relatório executivo de 2025`.

Próximo passo: Aula 21, o projeto final e a atualização do currículo.
