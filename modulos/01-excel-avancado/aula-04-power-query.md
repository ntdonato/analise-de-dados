# Aula 04: Power Query, limpando dados sem retrabalho

**Objetivo:** transformar o relatório "sujo" do sistema de caixa numa tabela limpa, com passos que se repetem sozinhos no mês seguinte.

**Tempo:** cerca de 3 horas. **Arquivo:** `dados/export_pdv_dez2025.csv`.

## Analogia

Todo mês você recebia um PDF ou planilha do sistema e fazia a mesma faxina: apagar o cabeçalho, arrumar o valor, tirar linhas repetidas. O **Power Query** é como gravar essa faxina numa receita. No mês seguinte, você troca o arquivo e aperta **Atualizar**. A receita roda inteira sozinha.

Onde a analogia quebra: a receita só funciona se o arquivo novo vier no mesmo formato. Se o sistema mudar o nome de uma coluna, a receita para naquele passo e avisa.

## O que é de verdade

Power Query é a ferramenta de **ETL** do Excel e do Power BI:

- **E**xtrair: ler os dados de um arquivo, pasta, banco ou site.
- **T**ransformar: limpar, mudar tipos, juntar, remover duplicadas.
- **L**oad (carregar): mandar o resultado limpo para uma Tabela.

Cada clique vira um passo na lista **Etapas Aplicadas**, à direita. Por baixo, o Excel escreve a receita numa linguagem chamada **M**. Você não precisa escrever M agora, mas vale abrir o **Editor Avançado** para ver.

O que você aprender aqui serve igualzinho no Power BI (Módulo 5).

## Mão na massa

Abra o arquivo no Bloco de Notas primeiro e observe os problemas:

- 3 linhas de título antes do cabeçalho;
- separador `;`;
- valores como `R$ 1.234,56` (texto, não número);
- formas de pagamento com espaços e em MAIÚSCULAS às vezes;
- algumas vendas repetidas.

### Eu faço: importar e tirar o cabeçalho

1. `Dados > Obter Dados > De Arquivo > De Texto/CSV`, escolha o arquivo e clique em **Transformar Dados** (não em Carregar).
2. `Página Inicial > Remover Linhas > Remover Linhas Superiores` > 3.
3. `Página Inicial > Usar a Primeira Linha como Cabeçalho`.

Olhe as Etapas Aplicadas: cada ação virou um passo. Clique num passo antigo para "voltar no tempo" e ver como a tabela estava.

### Fazemos juntos: arrumar textos e números

1. Selecione `Forma Pgto` > `Transformar > Formatar > Aparar` (tira os espaços). Depois `Formatar > ______` (deixa a primeira letra de cada palavra maiúscula).
2. Selecione `Valor` > `Transformar > Substituir Valores`: troque `R$ ` por nada.
3. Ainda em `Valor`: botão direito > `Alterar Tipo > Usando Localidade` > Número Decimal, localidade **Português (Brasil)**. Isso entende a vírgula como decimal.
4. Em `Data`: `Alterar Tipo > Usando Localidade` > Data, Português (Brasil).

Pergunta: por que mudar o tipo "usando localidade" em vez do jeito normal? O que aconteceria com `1.234,56` se o Excel achasse que está em inglês?

### Você faz

1. Remova as vendas duplicadas usando a coluna `Documento`.
2. Carregue para uma Tabela (`Fechar e Carregar`).
3. Monte uma tabela dinâmica com o total por forma de pagamento.
4. Confira: a soma de `Valor` deve bater **exatamente** com o total de dezembro/2025 da `tbVendas` (use o SOMASES da Aula 03).

Se não bater, algum passo ficou faltando. Volte nas Etapas Aplicadas e procure.

## Checagem

1. Explique ETL para alguém da recepção, em duas frases.
2. Quantas linhas o arquivo tinha antes de remover duplicadas, e quantas depois?
3. No mês que vem chega `export_pdv_jan2026.csv`. O que você precisa fazer para limpar?

## No seu portfólio

Salve `meus-arquivos/aula-04-power-query.xlsx`. No `progresso-aprendizado.md`, liste os passos da sua receita. Commit: `Aula 04: limpeza de export do PDV com Power Query`.

Com isso você pode marcar **Excel avançado** como concluído.

Próximo passo: Aula 05, estatística descritiva.
