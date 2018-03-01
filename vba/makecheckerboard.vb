Sub MakeCheckerboard()

  Dim color_options(1) As Integer
  color_options(0) = 22
  color_options(1) = 19

  Dim columnnumber as Integer
  Dim rownumber as Integer
  rownumber = 1
  columnnumber = 1

    ' Create a for loop from 1 to 10
    For i = 1 To 8

      For j = 1 To 8

          ' Use the modulus function to determine if a number is divisible by 2 (even number)
          If rownumber Mod 2 = 0 Then

              ' color
              Cells(i, 2).Value = "Even Row"
              
          ' If the number is not divisible by 2 (odd number)
          Else

              ' Enter "Even Row" the adjacent cell
              Cells(i, 2).Value = "Odd Row"
              
          ' Close the If/Else Statement
          End If

        rownumber = rownumber + 1
      
      Next j
    
      columnnumber = columnnumber + 1
    
    Next i

End Sub