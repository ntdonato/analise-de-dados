# Gabarito: Módulo 7 (VBA)

## Aula 18
Fazemos juntos: `.Font.Bold = True` e `ws.Range("H2:H" & ultimaLinha)`.

Checagem
1. Porque o gravador anota endereços fixos (ex.: `A1:H500`). Com outro número de linhas, sobra ou falta.
2. Export bagunçado: Power Query (é transformação de dados e repete com um clique). PDF por dia: VBA (é uma ação no Excel que o Power Query não faz).
3. O Excel avisa que vai apagar as macros. O arquivo fica sem o código.

## Aula 19
- Eu faço: Crédito em 24/12/2025 = R$ 1.047,30.
- Fazemos juntos: `UBound(formas)`, `formas(i)`, `"Divergência"`.
- Resultado de 24/12/2025 (sistema): Crédito R$ 1.047,30 · Débito R$ 1.050,42 · PIX R$ 901,21 · Dinheiro R$ 311,53 · Lançado no quarto R$ 769,40 · **Total R$ 4.079,86**. Com os valores de exemplo, só Dinheiro diverge (−R$ 10,00).

O arquivo `gabarito/FechamentoCaixa.bas` está salvo na codificação do Windows (ANSI), que é a que o editor do VBA usa. Por isso os acentos podem aparecer estranhos no GitHub, mas importam certo no Excel.

Checagem
1. O SOMASES não acha nada e devolve zero: aparece uma "divergência" falsa. Proteções: ler a lista de formas de uma aba de cadastro (e não digitada no código), ou validar com `CountIfs` se a forma existe antes de somar.
2. Sem data válida, o SOMASES compara com vazio e todos os valores dão zero. A macro "funciona", mas o resultado é falso.
3. "Ele monta uma tabela com todos os dias do mês, mostrando quanto entrou em cada forma de pagamento e o total do dia. Serve para conferir o mês inteiro de uma vez."
