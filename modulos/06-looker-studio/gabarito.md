# Gabarito: Módulo 6 (Looker Studio)

- Fazemos juntos: `SUM(valor_total) / COUNT(id_venda)`.
- Os totais devem bater com os outros módulos: 2025 = R$ 1.309.451,42, ticket R$ 100,50. Com comparação de ano anterior: +6,3%.
- Se o realizado de um mês aparecer multiplicado no blend, a junção está repetindo linhas: confira se a chave é `ano_mes` nos dois lados e se o tipo de junção é **Externa esquerda** a partir das vendas agregadas.

Checagem
1. Looker: painel simples e rápido de compartilhar por link, dados já no Google (Sheets, BigQuery), equipe sem licença do Power BI. Power BI: modelo com várias tabelas, cálculos complexos (DAX), bases grandes, empresa que usa Microsoft.
2. É juntar duas fontes por um campo em comum, como o JOIN do SQL ou o merge do pandas.
3. Porque no seu navegador você está logado e vê tudo. Na janela anônima você enxerga o que o recrutador vai ver.
