# Aula 03: PROCX e SOMASES, a planilha de metas × realizado

**Objetivo:** montar uma planilha de metas que se calcula sozinha: meta do mês, realizado, % atingido e quanto precisa vender por dia para bater a meta.

**Tempo:** cerca de 3 horas. **Arquivo:** `dados/loja.xlsx` (abas `vendas` e `metas_mensais`).

Você já fez algo parecido no trabalho. A diferença agora é usar as funções que as vagas pedem pelo nome.

## Analogia

- **SOMASES** é o conferente que só soma os comprovantes que passam em **todos** os critérios: "some só os de crédito, só da Loja, só de julho".
- **PROCX** é procurar um hóspede na lista pelo número do quarto e trazer o nome dele. Você diz o que procurar, onde procurar e o que trazer de volta.

Onde a analogia quebra: o PROCX traz só **o primeiro** que encontrar. Se houver dois hóspedes no mesmo quarto, ele traz um deles e ignora o outro.

## O que é de verdade

```
=SOMASES(o_que_somar; onde_olhar_1; critério_1; onde_olhar_2; critério_2; ...)
=PROCX(o_que_procurar; onde_procurar; o_que_devolver; [se_não_achar])
```

Com Tabelas, você escreve com nomes em vez de endereços: `tbVendas[valor_total]` em vez de `H2:H25316`. Fica mais fácil de ler e não quebra quando a base cresce.

## Mão na massa

Prepare: salve uma cópia de `loja.xlsx` como `aula-03-metas.xlsx`. As Tabelas `tbVendas` e `tbMetas` já existem. Em `tbVendas`, crie a coluna `ano_mes` com `=TEXTO([@data];"aaaa-mm")`.

Crie uma aba `Painel` com esta estrutura:

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | ano_mes | Meta | Realizado | % atingido | Situação |
| 2 | 2025-01 | | | | |
| ... | ... | | | | |
| 13 | 2025-12 | | | | |

### Eu faço: realizado do mês

Em C2:

```
=SOMASES(tbVendas[valor_total]; tbVendas[ano_mes]; A2)
```

Lendo em voz alta: "some a coluna valor_total, só nas linhas em que ano_mes é igual ao que está em A2". Arraste até C13.

### Fazemos juntos: meta e % atingido

Em B2, complete:

```
=PROCX(A2; tbMetas[______]; tbMetas[______]; "sem meta")
```

Em D2: `=C2/B2`, formatado como porcentagem.

Em E2, use SE para escrever "Bateu" ou "Não bateu":

```
=SE(D2>=______; "Bateu"; "Não bateu")
```

Depois aplique **Formatação Condicional** em E2:E13: verde para "Bateu", vermelho para "Não bateu".

### Você faz: a projeção diária

Na planilha do hotel você calculava "meta restante dividida pelos dias restantes". Agora faça isso de forma automática para **um mês escolhido**:

1. Numa célula H1, digite uma data de referência, ex.: `15/07/2025`.
2. Calcule:
   - Realizado do mês **até** a data (SOMASES com dois critérios na data: `">="&início do mês` e `"<="&H1`).
   - Dias restantes no mês: use `FIMMÊS(H1;0)-H1`.
   - Valor por dia necessário: (meta − realizado até a data) ÷ dias restantes.

Resultado esperado: um número em R$ por dia que muda quando você troca a data em H1.

Desafio extra: some só o canal "Online" de 2025 usando SOMASES com dois critérios.

## Checagem

1. Na fórmula do PROCX, o que acontece se o mês não existir em `tbMetas`? Por que o quarto argumento é útil?
2. Quantos meses de 2025 bateram a meta? E de 2024?
3. Por que `tbVendas[valor_total]` é melhor que `H2:H25316`?

## No seu portfólio

Salve `meus-arquivos/aula-03-metas.xlsx`. Tire um print da aba Painel e salve como `meus-arquivos/aula-03-painel.png`. Commit: `Aula 03: painel de metas com PROCX e SOMASES`.

Próximo passo: Aula 04, Power Query.
