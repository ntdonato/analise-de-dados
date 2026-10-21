# Gabarito: Módulo 5 (Power BI)

## Aula 14
- Fazemos juntos: a chave é `id_venda`; Externa esquerda = **LEFT** JOIN.
- Teste: 2024 = R$ 1.232.094,15 · 2025 = R$ 1.309.451,42.

Checagem
1. Ex.: fato = check-ins (um por hospedagem, muitas linhas, com data e valor); dimensões = hóspedes, quartos e calendário (cadastros).
2. Porque relação entre duas tabelas fato deixa o filtro confuso e lento. Com a data em `fItens`, as duas tabelas fato ficam ligadas no mesmo calendário, formando a estrela.
3. Classificar a coluna `Mes` pela coluna `MesNum`.

## Aula 15

```DAX
Meta = SUM ( fMetas[meta] )
% Meta = DIVIDE ( [Faturamento], [Meta] )
Faturamento AA = CALCULATE ( [Faturamento], SAMEPERIODLASTYEAR ( dCalendario[Date] ) )
Var % AA = DIVIDE ( [Faturamento] - [Faturamento AA], [Faturamento AA] )
Acumulado Mês = TOTALMTD ( [Faturamento], dCalendario[Date] )
Receita Itens = SUM ( fItens[valor_item] )
Custo = SUMX ( fItens, fItens[quantidade] * RELATED ( dProdutos[custo_unitario] ) )
Margem % = DIVIDE ( [Receita Itens] - [Custo], [Receita Itens] )
Faturamento Online = CALCULATE ( [Faturamento], fVendas[canal] = "Online" )
% Online = DIVIDE ( [Faturamento Online], [Faturamento] )
```

Conferências: dez/2025 → % Meta 94,1% e Var % AA +11,4%. Acumulado de julho/2025 → R$ 145.724,00 no dia 31. Margem % de 2025 → Cafeteria 68,1%. % Online em 2025 → 8,1%.

Checagem
1. Coluna calculada: calculada linha a linha e guardada (ex.: faixa de preço do produto). Medida: calculada na hora conforme o filtro (ex.: faturamento, ticket).
2. Calcula uma medida trocando ou acrescentando filtros. Ex.: "faturamento, mas só do Online" ou "do ano passado".
3. Porque não dá erro de divisão por zero: devolve vazio.

## Aula 16
- Fazemos juntos: eixo X `dCalendario[Mes]` (com o filtro de Ano), linha `[Meta]`.

Checagem
1. Porque lemos em Z: é o primeiro lugar que o olho vê.
2. Os visuais que não respondem a nenhuma pergunta do gerente. Deixe os cartões, a linha de meta e um detalhe.
3. "2024 bateu a meta em 8 dos 12 meses".
