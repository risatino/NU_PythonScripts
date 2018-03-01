Sub CopyRow()

'Selection.Copy Sheets("Blank BOM").Cells(Rows.Count, 1).End(xlUp).Offset(1, 0)

Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets.Add(After:= _
    ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count))
    ws.Name = "Combined"
    
With Sheets("Combined")
    Selection.Copy .Cells(.Rows.Count, 1).End(xlUp).Offset(1, 0)
End With

    Sub Copy_to_Range()
    
        Worksheets("Sample Data").Range("B5:M107").Copy _
            Destination:=Worksheets("Example 2 - Destination").Range("B5:M107")
            
        Worksheets("Example 2 - Destination").Columns("B:M").AutoFit
            
    End Sub
   
End Sub

' ********************************************************The Answer

' Steps:
' ----------------------------------------------------------------------------

' Part II:

' 1. Loop through every worksheet and select the state contents.
' 2. Copy the state contents and paste it into the Combined_Data tab

Sub WellsFargo_PtII()
    
    ' last row in combined worksheet
    Dim lastRowCombined As Integer

    ' first row in all worksheets
    Dim firstRow As Integer
    firstRow = 2

    ' last row in current worksheet
    Dim lastRow As Integer

    ' number of rows in current worksheet
    Dim nRows As Integer

    ' Specify the location of the combined sheet
    Set combined_sheet = Worksheets("Combined_Data")

    ' Loop through all sheets
    For Each ws In Worksheets

        If ws.Name <> "Combined_Data" Then

            ' Find the last row of the combined sheet after each paste
            lastRowCombined = combined_sheet.Cells(Rows.Count, "A").End(xlUp).Row

            ' Find the last row in current worksheet
            lastRow = ws.Cells(Rows.Count, "A").End(xlUp).Row

            ' Calculate the number of rows in current worksheet (last row - first row + 1)
            nRows = lastRow - firstRow + 1

            ' Copy the contents of each state sheet into the combined sheet
            combined_sheet.Range("A" & lastRowCombined + 1 & ":G" & lastRowCombined + nRows).Value = ws.Range("A2:G" & lastRow).Value

        End If

    Next ws
End Sub



