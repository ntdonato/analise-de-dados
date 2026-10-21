# Gabarito: Módulo 1 (Excel avançado)

Só abra depois de responder no seu `progresso-aprendizado.md`.

## Aula 02

**Fazemos juntos:** forma de pagamento vai em **Colunas**; a opção é **Mostrar Valores Como > % do Total Geral** (ou "% do Total da Linha", se o mês estiver nas linhas).

Em 2025: Crédito 41,2% · PIX 25,6% · Débito 17,4% · Lançado no quarto 11,3% · Dinheiro 4,5%.

**Você faz:** sexta, sábado e domingo faturam cerca de R$ 225 mil cada em 2025. Segunda fatura cerca de R$ 147 mil.

**Checagem**
1. A Tabela cresce sozinha quando entram linhas novas, então a tabela dinâmica pega tudo ao atualizar. Com um intervalo fixo (A1:H25316), as linhas novas ficam de fora.
2. Faltou clicar em **Atualizar** (Analisar > Atualizar, ou Alt+F5).
3. Por exemplo: canal nas Linhas, ano nas Colunas, soma e contagem de vendas nos Valores. Depois compare o ticket médio (Média de valor_total) de cada canal. Online faturou R$ 106.129,56 em 2025, cerca de 8% do total.

## Aula 03

**Fazemos juntos**
```
=PROCX(A2; tbMetas[ano_mes]; tbMetas[meta]; "sem meta")
=SE(D2>=1; "Bateu"; "Não bateu")
```
(1 = 100% quando a célula está formatada como porcentagem.)

**Você faz** (data de referência 15/07/2025)
- Meta de jul/2025: R$ 150.000
- Realizado de 01/07 a 15/07: R$ 68.112,18
- Dias restantes: `FIMMÊS(H1;0)-H1` = 16
- Necessário por dia: R$ 5.117,99

Fórmula do realizado até a data:
```
=SOMASES(tbVendas[valor_total]; tbVendas[data]; ">="&DATA(ANO(H1);MÊS(H1);1); tbVendas[data]; "<="&H1)
```

Desafio extra: Online em 2025 = R$ 106.129,56.

**Checagem**
1. Sem o quarto argumento aparece `#N/D`. Com ele, aparece o texto que você escolheu ("sem meta"), o que deixa claro que falta cadastrar.
2. 2025: 6 meses bateram (jan, mar, abr, ago, set, out). 2024: 8 meses.
3. Lê-se melhor, e a fórmula acompanha a Tabela quando ela cresce.

## Aula 04

- Antes de remover duplicadas: 1.747 linhas. Depois: 1.735.
- Total de dez/2025 depois de limpo: **R$ 202.382,25** (igual à `tbVendas`).

**Pergunta do "fazemos juntos":** a opção é **Colocar Cada Palavra em Maiúscula**. Mudar o tipo "usando localidade" diz ao Excel que a vírgula é decimal e o ponto é milhar. Em inglês, `1.234,56` viraria erro ou um número errado.

**Checagem**
1. Exemplo: "ETL é pegar os dados de onde estão, arrumar e entregar prontos para análise. É a faxina do relatório do sistema, só que gravada para repetir sozinha."
2. 1.747 e 1.735.
3. Trocar a origem (Página Inicial > Configurações da Fonte de Dados > Alterar Fonte) para o arquivo novo e clicar em Atualizar.
