# Aula 18: Macros, gravando e lendo seu primeiro VBA

**Objetivo:** gravar uma macro que formata o relatório do caixa com um clique, e entender o código que o Excel escreveu.

**Tempo:** cerca de 2h30. **Arquivo:** `dados/loja.xlsx`, aba `vendas`.

## Revisão rápida

1. Que tarefa repetitiva o Power Query resolve? (Aula 04)
2. O que é uma receita "repetível"?

## Analogia

Uma **macro** é como ensinar uma tarefa a um estagiário filmando você fazer. Você aperta "gravar", faz a formatação uma vez, e o Excel anota cada passo. Depois, o estagiário repete tudo com um clique.

O **VBA** (*Visual Basic for Applications*) é a língua em que essas anotações são escritas. Lendo o que foi gravado, você aprende a escrever as suas próprias.

Onde a analogia quebra: o gravador anota **exatamente** o que você fez, inclusive cliques desnecessários e endereços fixos (`Range("A1:H500")`). Se amanhã o relatório tiver 600 linhas, a macro gravada formata só 500. Por isso aprendemos a editar.

Power Query × VBA: o Power Query é melhor para **limpar e transformar dados**. O VBA é melhor para **ações no Excel**: formatar, criar abas, gerar PDF, enviar relatórios, mexer em vários arquivos.

## O que é de verdade

```vba
Sub NomeDaMacro()
    ' comentário: começa com apóstrofo
    Range("A1").Value = "Olá"
End Sub
```

- `Sub ... End Sub`: o começo e o fim de uma macro.
- `Range("A1")`: uma célula ou intervalo.
- `.Value`, `.Font.Bold`, `.Interior.Color`: propriedades (características) da célula.
- O arquivo precisa ser salvo como **.xlsm** (pasta de trabalho habilitada para macro).

## Mão na massa

### Preparar

1. Ative a guia **Desenvolvedor**: `Arquivo > Opções > Personalizar Faixa de Opções` > marque **Desenvolvedor**.
2. Abra `loja.xlsx`. Clique com o botão direito na aba `vendas` > **Mover ou copiar** > Para pasta: **(nova pasta)**, marque **Criar uma cópia**. Na pasta nova, clique na Tabela e use `Design da Tabela > Converter em Intervalo`, depois `Página Inicial > Limpar > Limpar Formatos`. Agora você tem um "relatório cru", como os que vêm do sistema.
3. Salve essa pasta nova como `aula-18-macros.xlsm`.

### Eu faço: gravar

1. `Desenvolvedor > Gravar Macro`. Nome: `FormatarRelatorio`. OK.
2. Faça a formatação: cabeçalho em negrito com fundo verde-escuro e letra branca; coluna H em formato Moeda; **Congelar Painéis** na linha 1; autoajuste das colunas (selecione A:H e dê duplo clique na divisa).
3. `Desenvolvedor > Parar Gravação`.
4. Abra o editor com **Alt+F11**. Em `Módulos > Módulo1`, veja o código gravado.

### Fazemos juntos: limpar o código gravado

O gravador escreve muito `Select` e `Selection`. Reescreva a macro assim, completando as lacunas:

```vba
Sub FormatarRelatorio()
    Dim ws As Worksheet
    Dim ultimaLinha As Long

    Set ws = ActiveSheet
    ultimaLinha = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row   ' acha a última linha com dados

    With ws.Range("A1:H1")
        .Font.Bold = ______
        .Font.Color = RGB(255, 255, 255)
        .Interior.Color = RGB(13, 107, 102)
    End With

    ws.Range("H2:H" & __________).NumberFormat = "R$ #,##0.00"
    ws.Columns("A:H").AutoFit
End Sub
```

- `Dim`: cria uma variável (uma "caixinha" com nome).
- `ws.Cells(ws.Rows.Count, "A").End(xlUp).Row`: vai até a última linha da planilha e "sobe" até achar dado. É o Ctrl+↑ do teclado. Assim a macro funciona com qualquer tamanho de relatório.
- `With ... End With`: evita repetir `ws.Range("A1:H1")` em cada linha.

Rode com **F5** no editor, numa cópia sem formatação.

### Você faz

1. Acrescente à macro: **AutoFiltro** no cabeçalho (`ws.Range("A1:H1").AutoFilter`) e a planilha renomeada para `Vendas`.
2. Crie um **botão**: `Inserir > Formas`, desenhe um retângulo, escreva "Formatar", clique com o botão direito > **Atribuir Macro** > `FormatarRelatorio`.
3. Teste num relatório de outro tamanho: copie a aba, apague todas as linhas de 2025 e rode a macro de novo. A formatação deve ir até a última linha, nem mais nem menos.

## Checagem

1. Por que a macro gravada pode falhar quando o relatório muda de tamanho?
2. Para limpar um export bagunçado do sistema, você usaria Power Query ou VBA? E para gerar um PDF por dia? Por quê?
3. O que acontece se você salvar como `.xlsx` em vez de `.xlsm`?

## No seu portfólio

Exporte o módulo: no editor, botão direito em `Módulo1` > **Exportar arquivo** > `projetos/p5-vba-fechamento-caixa/FormatarRelatorio.bas`. Um `.bas` é texto, então o GitHub mostra o código. Commit: `Aula 18: primeira macro VBA`.

Próximo passo: Aula 19, VBA com laços e o fechamento de caixa automático.
