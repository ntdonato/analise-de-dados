# Aula 06: Variação entre períodos e correlação

**Objetivo:** responder "crescemos em relação ao ano passado?" e "o faturamento sobe porque vendemos mais vezes ou porque cada venda é maior?".

**Tempo:** cerca de 3 horas. **Arquivo:** o `aula-03-metas.xlsx` (Tabela `tbVendas` e aba `Painel`).

## Analogia

- **Variação percentual** é como comparar a ocupação do hotel neste julho com o julho passado. Comparar julho com março não faz sentido, porque julho é alta temporada. Por isso se compara **o mesmo mês do ano anterior** (em inglês, YoY: *year over year*).
- **Correlação** é perceber que, nos dias de mais check-ins, o café da manhã também lota. As duas coisas andam juntas.

Onde a analogia quebra: andar junto não prova que uma coisa causa a outra. Sorvete e guarda-chuva podem ter correlação negativa por causa do clima, sem um causar o outro. Correlação não é causa.

## O que é de verdade

**Variação %** = (valor atual ÷ valor anterior) − 1.

**Coeficiente de correlação de Pearson** (`=CORREL()`) vai de −1 a 1:

| Valor | Leitura |
|---|---|
| perto de 1 | sobem juntas |
| perto de 0 | não têm relação linear |
| perto de −1 | uma sobe, a outra desce |

**Coeficiente de variação** (CV) = desvio padrão ÷ média. Diz se a variação é grande *em relação ao tamanho* do número. Bom para comparar a estabilidade de coisas de tamanhos diferentes.

## Mão na massa

### Eu faço: crescimento ano contra ano

Na aba `Painel`, ao lado de 2025, traga 2024 e calcule:

| ano_mes | Realizado 2025 | Realizado 2024 | Variação % |
|---|---|---|---|
| jan | `=SOMASES(...;"2025-01")` | `=SOMASES(...;"2024-01")` | `=B2/C2-1` |

Formate a variação como porcentagem, com formatação condicional de **Escala de Cores**. Some os 12 meses e calcule a variação do ano inteiro.

### Fazemos juntos: correlação no dia a dia

1. Monte uma tabela dinâmica de 2025 com `data` nas linhas (sem agrupar por mês, um dia por linha), **Contagem** de id_venda e **Soma** de valor_total nos valores.
2. Copie e cole como valores numa aba nova (colunas `dia`, `n_vendas`, `faturamento`).
3. Calcule `=CORREL(______; ______)` entre número de vendas e faturamento do dia.
4. Faça um **gráfico de dispersão** (`Inserir > Dispersão`) com n_vendas no eixo X e faturamento no Y. Adicione **Linha de Tendência**.

### Você faz

1. Calcule o faturamento médio diário, o desvio padrão diário e o CV. A loja é estável ou varia muito de um dia para o outro?
2. Crie uma coluna `fim_de_semana` (sexta a domingo = 1, senão 0) e compare a média diária dos dois grupos. Quantos % a mais vende um dia de fim de semana?
3. Escreva uma conclusão de 3 linhas: "O crescimento de 2025 veio de quê?".

## Checagem

1. Por que comparar dezembro/2025 com dezembro/2024 e não com novembro/2025?
2. A correlação entre número de vendas e faturamento deu cerca de 0,9. O que isso diz? E o que **não** diz?
3. O que significa um CV de 0,47 para o faturamento diário?

## No seu portfólio

Salve `meus-arquivos/aula-06.xlsx` e o gráfico de dispersão. Commit: `Aula 06: crescimento YoY e correlação`.

Com isso você pode marcar **Estatística descritiva** como concluída.

Próximo passo: Aula 07, primeiros passos em SQL.
