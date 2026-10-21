# Gabarito: Módulo 2 (Estatística)

## Aula 05 (vendas de 2025)

| Medida | Valor |
|---|---|
| Nº de vendas | 13.030 |
| Média | R$ 100,50 |
| Mediana | R$ 69,90 |
| Desvio padrão | R$ 100,29 |
| Mínimo / Máximo | R$ 4,41 / R$ 1.008,60 |
| Q1 / Q3 | R$ 26,14 / R$ 139,80 |
| IQR | R$ 113,66 |
| Limite superior | R$ 310,29 |
| Outliers | 564 vendas |

(Pequenas diferenças nos centavos podem vir do método de quartil. `QUARTIL.INC` deve bater.)

**Fazemos juntos:** `QUARTIL.INC(A2#;1)`, `QUARTIL.INC(A2#;3)`, `IQR = Q3 − Q1`, `Limite = Q3 + 1,5 * IQR`.

**Você faz:** o histograma tem cauda longa à direita: muitas vendas pequenas e poucas grandes. Média e mediana por canal são quase iguais (mediana R$ 69,90 nos três). O canal não muda o ticket.

**Checagem**
1. Porque algumas vendas grandes (kits, cestas) puxam a média para cima. A mediana não se mexe com elas.
2. Outlier não é erro: são vendas reais e valiosas. Apagar distorce o faturamento. O certo é reportar a mediana junto e, se quiser, analisar os outliers à parte.
3. Que todas as vendas teriam exatamente o mesmo valor.

## Aula 06

Variação 2025 × 2024 por mês: jan +13,4% · fev +6,1% · mar +0,8% · abr +4,6% · mai +7,1% · jun +7,2% · jul +4,1% · ago +6,3% · set +7,1% · out +0,7% · nov +3,8% · dez +11,4%. **Ano: +6,3%.**

Correlação nº de vendas × faturamento diário em 2025: **0,90**.

Faturamento diário 2025: média R$ 3.587,54 · desvio padrão R$ 1.699,74 · CV 0,47.

**Você faz 2:** média diária de sexta a domingo R$ 4.347,81; de segunda a quinta R$ 3.020,06. Um dia de fim de semana vende cerca de **44% a mais**.

**Você faz 3:** o ticket médio ficou praticamente igual (R$ 100,29 em 2024 e R$ 100,50 em 2025), e o número de vendas subiu de 12.285 para 13.030. O crescimento veio de **mais vendas**, não de vendas maiores.

**Checagem**
1. Por causa da sazonalidade: dezembro é sempre alto (Natal). Comparar com novembro misturaria o efeito da época com o crescimento real.
2. Diz que, em dias com mais vendas, o faturamento quase sempre é maior. Não diz que é só isso que explica o faturamento, nem prova causa.
3. Que o desvio típico em torno da média diária é quase metade dela: há muita variação entre dias (fins de semana e alta temporada).
