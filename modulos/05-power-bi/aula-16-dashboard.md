# Aula 16: Montando o dashboard

**Objetivo:** publicar um dashboard de uma página que responde, em 10 segundos: "estamos batendo a meta? o que vende? quando vende?".

**Tempo:** cerca de 4 horas (inclui o Projeto 3).

## Revisão rápida

1. Escreva de cabeça a medida de ticket médio.
2. O que `SAMEPERIODLASTYEAR` precisa para funcionar?

## Analogia

O dashboard é o **painel do carro**. O motorista não quer ver o motor; quer saber velocidade, combustível e se alguma luz acendeu. Os números mais importantes ficam grandes e no alto; os detalhes, embaixo.

Onde a analogia quebra: o painel do carro não deixa você filtrar. O dashboard deixa: o gerente clica em "Online" e tudo se recalcula para o Online.

## O que é de verdade

Layout em **Z**, porque é assim que lemos uma página:

```
┌───────────────────────────────────────────────────┐
│ Título com a conclusão          [Ano] [Canal]     │  filtros
├──────────┬──────────┬──────────┬──────────────────┤
│Faturamento│ % Meta  │ Ticket   │ Var % AA         │  cartões (KPIs)
├──────────┴──────────┴──────────┴──────────────────┤
│ Linha: realizado × meta por mês                   │  tendência
├─────────────────────────┬─────────────────────────┤
│ Barras: categorias      │ Matriz: canal × dia     │  detalhe
└─────────────────────────┴─────────────────────────┘
```

Regras: no máximo 6 a 8 visuais; uma cor de destaque; verde e vermelho só para bom e ruim; títulos que digam a conclusão.

## Mão na massa

### Eu faço: os cartões

1. Insira 4 visuais de **Cartão** com `Faturamento`, `% Meta`, `Ticket Médio` e `Var % AA`.
2. Insira 2 **Segmentações de dados**: `dCalendario[Ano]` (estilo Bloco) e `fVendas[canal]` (Lista suspensa).
3. Em `% Meta`, use **Formatação condicional** na cor do texto: vermelho abaixo de 1, verde a partir de 1.

### Fazemos juntos: realizado × meta

1. Insira um **Gráfico de colunas e linhas**.
2. Eixo X: `dCalendario[______]`. Colunas: `[Faturamento]`. Linha: `[______]`.
3. Título: escreva a conclusão, não o nome do gráfico. Ex.: "2025 bateu a meta em 6 dos 12 meses".

### Você faz

1. Barras horizontais com `Receita Itens` por `dProdutos[categoria]`, ordenadas, com rótulos de dados.
2. Matriz com `fVendas[canal]` nas linhas, `dCalendario[DiaSemana]` nas colunas e `Faturamento` nos valores, com **escala de cores** de fundo (mapa de calor).
3. Uma página extra de **detalhe** com o acumulado diário (Aula 15) e uma tabela com os 10 produtos que mais faturam.
4. Teste os filtros: clique em "Online". Todos os visuais mudam juntos?

### Publicar

- **Opção grátis e garantida:** `Arquivo > Exportar > PDF` e prints das páginas. Coloque no README do Projeto 3.
- **Publicar na web:** precisa de uma conta Power BI de trabalho ou escola (e-mail pessoal do Gmail não serve). Se tiver o e-mail do IFRS, tente: `Publicar` e, no serviço online, `Arquivo > Inserir relatório > Publicar na Web`. Coloque o link no README.

## Checagem

1. Por que os cartões ficam no alto, à esquerda?
2. O gerente diz: "tem gráfico demais, não entendo nada". O que você tira primeiro?
3. Escreva o título do gráfico realizado × meta para o ano de 2024.

## No seu portfólio

Siga o checklist do `projetos/p3-power-bi-dashboard/README.md`. Commit: `Projeto 3: dashboard de vendas no Power BI`.

Com o Projeto 3 publicado, você pode mover **Power BI** para Competências.

Próximo passo: Aula 17, Looker Studio.
