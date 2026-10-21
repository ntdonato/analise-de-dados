Attribute VB_Name = "FechamentoCaixa"
Option Explicit

' Gabarito da Aula 19 e do Projeto 5
' Planilhas esperadas:
'   "Vendas"     -> dados de vendas.csv (A:id_venda, B:data, C:hora, D:canal,
'                   E:forma_pagamento, F:bandeira, G:maquininha, H:valor_total)
'   "Fechamento" -> B1: data do fechamento; A4:A8 formas de pagamento;
'                   B: valor do sistema; C: valor contado; D: diferença; E: situação

Private Function FormasPagamento() As Variant
    FormasPagamento = Array("Crédito", "Débito", "PIX", "Dinheiro", "Lançado no quarto")
End Function

Sub FecharCaixa()
    Dim wsV As Worksheet, wsF As Worksheet
    Dim ultima As Long, i As Long, linha As Long
    Dim dataRef As Date, formas As Variant
    Dim rngData As Range, rngForma As Range, rngValor As Range
    Dim sistema As Double, contado As Double, diferenca As Double, totalDia As Double

    Set wsV = ThisWorkbook.Worksheets("Vendas")
    Set wsF = ThisWorkbook.Worksheets("Fechamento")

    If Not IsDate(wsF.Range("B1").Value) Then
        MsgBox "Digite uma data válida em B1.", vbExclamation
        Exit Sub
    End If
    dataRef = wsF.Range("B1").Value

    ultima = wsV.Cells(wsV.Rows.Count, "A").End(xlUp).Row
    Set rngData = wsV.Range("B2:B" & ultima)
    Set rngForma = wsV.Range("E2:E" & ultima)
    Set rngValor = wsV.Range("H2:H" & ultima)

    If Application.WorksheetFunction.CountIfs(rngData, dataRef) = 0 Then
        MsgBox "Não há vendas em " & Format(dataRef, "dd/mm/yyyy") & ".", vbInformation
        Exit Sub
    End If

    formas = FormasPagamento()
    totalDia = 0
    For i = LBound(formas) To UBound(formas)
        linha = 4 + i
        sistema = Application.WorksheetFunction.SumIfs(rngValor, rngData, dataRef, rngForma, formas(i))
        contado = Val(Replace(CStr(wsF.Cells(linha, "C").Value), ",", "."))
        diferenca = Round(contado - sistema, 2)

        wsF.Cells(linha, "A").Value = formas(i)
        wsF.Cells(linha, "B").Value = Round(sistema, 2)
        wsF.Cells(linha, "D").Value = diferenca

        If IsEmpty(wsF.Cells(linha, "C").Value) Then
            wsF.Cells(linha, "E").Value = "Falta contar"
            wsF.Cells(linha, "E").Interior.Color = RGB(255, 235, 156)
        ElseIf Abs(diferenca) < 0.01 Then
            wsF.Cells(linha, "E").Value = "OK"
            wsF.Cells(linha, "E").Interior.Color = RGB(198, 239, 206)
        Else
            wsF.Cells(linha, "E").Value = "Divergência"
            wsF.Cells(linha, "E").Interior.Color = RGB(255, 199, 206)
        End If
        totalDia = totalDia + sistema
    Next i

    wsF.Range("A10").Value = "Total do sistema"
    wsF.Range("B10").Value = Round(totalDia, 2)
    wsF.Range("B4:D10").NumberFormat = "R$ #,##0.00"
    wsF.Range("A12").Value = "Fechado em " & Format(Now, "dd/mm/yyyy hh:mm")
End Sub

Sub ResumoDoMes()
    ' Gera a aba "Resumo Mês": uma linha por dia do mês da data em Fechamento!B1,
    ' uma coluna por forma de pagamento, e o total.
    Dim wsV As Worksheet, wsR As Worksheet
    Dim ultima As Long, linha As Long, i As Long
    Dim inicio As Date, fim As Date, d As Date, formas As Variant
    Dim rngData As Range, rngForma As Range, rngValor As Range

    Set wsV = ThisWorkbook.Worksheets("Vendas")
    inicio = DateSerial(Year(ThisWorkbook.Worksheets("Fechamento").Range("B1").Value), _
                        Month(ThisWorkbook.Worksheets("Fechamento").Range("B1").Value), 1)
    fim = DateSerial(Year(inicio), Month(inicio) + 1, 0)   ' dia 0 do mês seguinte = último dia deste mês

    ultima = wsV.Cells(wsV.Rows.Count, "A").End(xlUp).Row
    Set rngData = wsV.Range("B2:B" & ultima)
    Set rngForma = wsV.Range("E2:E" & ultima)
    Set rngValor = wsV.Range("H2:H" & ultima)

    Application.DisplayAlerts = False
    On Error Resume Next
    ThisWorkbook.Worksheets("Resumo Mês").Delete
    On Error GoTo 0
    Application.DisplayAlerts = True

    Set wsR = ThisWorkbook.Worksheets.Add(After:=ThisWorkbook.Worksheets(ThisWorkbook.Worksheets.Count))
    wsR.Name = "Resumo Mês"

    formas = FormasPagamento()
    wsR.Range("A1").Value = "Data"
    For i = LBound(formas) To UBound(formas)
        wsR.Cells(1, 2 + i).Value = formas(i)
    Next i
    wsR.Cells(1, 3 + UBound(formas)).Value = "Total"

    linha = 2
    For d = inicio To fim
        wsR.Cells(linha, "A").Value = d
        For i = LBound(formas) To UBound(formas)
            wsR.Cells(linha, 2 + i).Value = Application.WorksheetFunction.SumIfs(rngValor, rngData, d, rngForma, formas(i))
        Next i
        wsR.Cells(linha, 3 + UBound(formas)).FormulaR1C1 = "=SUM(RC2:RC[-1])"
        linha = linha + 1
    Next d

    With wsR
        .Range("A2:A" & linha - 1).NumberFormat = "dd/mm/yyyy"
        .Range(.Cells(2, 2), .Cells(linha - 1, 3 + UBound(formas))).NumberFormat = "R$ #,##0.00"
        .Range(.Cells(1, 1), .Cells(1, 3 + UBound(formas))).Font.Bold = True
        .Columns.AutoFit
    End With
    MsgBox "Resumo de " & Format(inicio, "mm/yyyy") & " criado.", vbInformation
End Sub

Sub ExportarFechamentoPDF()
    Dim wsF As Worksheet, arquivo As String
    Set wsF = ThisWorkbook.Worksheets("Fechamento")
    arquivo = ThisWorkbook.Path & Application.PathSeparator & _
              "Fechamento_" & Format(wsF.Range("B1").Value, "yyyy-mm-dd") & ".pdf"
    wsF.ExportAsFixedFormat Type:=xlTypePDF, Filename:=arquivo
    MsgBox "PDF salvo em " & arquivo, vbInformation
End Sub
