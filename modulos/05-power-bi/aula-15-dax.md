# Aula 15: DAX, as fórmulas do Power BI

**Objetivo:** criar as medidas do painel de metas: faturamento, ticket médio, % da meta, comparação com o ano anterior, acumulado do mês e margem.

**Tempo:** cerca de 3h30.

## Revisão rápida

1. Para onde "anda" o filtro num relacionamento 1:\*?
2. Para que serve a tabela calendário?

## Analogia

Uma **medida** DAX é uma fórmula que não mora numa célula. Ela é recalculada para **cada pedaço** do visual onde você a coloca.

É como perguntar "quanto vendemos?" para o caixa. Se você está olhando julho, ele responde julho. Se está olhando a Loja em dezembro, ele responde a Loja em dezembro. A pergunta é sempre a mesma; o **contexto** muda a resposta.

Onde a analogia quebra: o caixa às vezes erra; a medida, não. Mas, se o modelo estiver mal ligado (Aula 14), ela responde certinho a pergunta errada.

## O que é de verdade

- **Coluna calculada:** calculada linha a linha, uma vez, e guardada. Use pouco.
- **Medida:** calculada na hora, conforme os filtros (contexto). Use para quase tudo que é número de painel.
- **CALCULATE:** a função mais importante. Ela calcula uma medida **mudando o contexto**. Ex.: "o faturamento, mas no mesmo período do ano passado".

Crie uma tabela vazia só para guardar as medidas: `Página Inicial > Inserir dados`, nome `_Medidas`, OK. Depois, com ela selecionada, `Nova medida`.

## Mão na massa

### Eu faço: medidas básicas

```DAX
Faturamento = SUM ( fVendas[valor_total] )

Nº Vendas = COUNTROWS ( fVendas )

Ticket Médio = DIVIDE ( [Faturamento], [Nº Vendas] )
```

- `SUM` soma a coluna no contexto atual.
- `COUNTROWS` conta as linhas.
- `DIVIDE(a, b)` divide e devolve vazio em vez de erro quando b é zero. Use sempre no lugar de `/`.

Formate: selecione a medida e, em `Ferramentas de medida`, escolha Moeda (R$) ou número inteiro.

Teste num visual de tabela com `dCalendario[Mes]`: a mesma medida muda em cada linha. Isso é o contexto.

### Fazemos juntos: metas e ano anterior

```DAX
Meta = SUM ( fMetas[______] )

% Meta = DIVIDE ( [Faturamento], [______] )

Faturamento AA =
CALCULATE ( [Faturamento], SAMEPERIODLASTYEAR ( dCalendario[______] ) )

Var % AA = DIVIDE ( [Faturamento] - [Faturamento AA], [__________] )
```

`AA` = ano anterior. `SAMEPERIODLASTYEAR` só funciona porque `dCalendario` foi marcada como tabela de data.

Teste: em dezembro de 2025, `% Meta` deve dar 94,1% e `Var % AA`, +11,4%.

### Você faz

1. **Acumulado do mês** (a coluna ACUMULADO da sua planilha): use `TOTALMTD ( [Faturamento], dCalendario[Date] )`. Coloque num gráfico de linha com os dias de julho/2025.
2. **Margem:**
   ```DAX
   Receita Itens = SUM ( fItens[valor_item] )
   Custo = SUMX ( fItens, fItens[quantidade] * RELATED ( dProdutos[custo_unitario] ) )
   ```
   Crie `Margem %` com `DIVIDE`. `SUMX` calcula linha a linha e depois soma; `RELATED` busca o custo na tabela de produtos pela relação.
3. **Desafio:** `Faturamento Online = CALCULATE ( [Faturamento], fVendas[canal] = "Online" )` e `% Online` sobre o total.

## Checagem

1. Qual a diferença entre medida e coluna calculada? Dê um exemplo de quando usar cada uma.
2. O que o `CALCULATE` faz, com suas palavras?
3. Por que `DIVIDE` é melhor que `/`?

## No seu portfólio

Salve o `.pbix`. Copie todas as medidas para `projetos/p3-power-bi-dashboard/medidas.dax` (texto), para o recrutador ler sem abrir o Power BI. Commit: `Aula 15: medidas DAX de metas, AA e margem`.

Próximo passo: Aula 16, montar o dashboard.
