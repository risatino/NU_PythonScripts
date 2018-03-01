Sub ChessBoard()

  ' Using Ranges
  ' ---------------------------------------

  ' Insert Pawns
  Range("A2:H2").Value = "Pawn"

  ' Insert Rooks
  Range("A1", "H1").Value = "Rook"

  ' Insert Knights
  Range("B1", "G1").Value = "Knight"

  ' Insert Bishops
  Range("C1", "F1").Value = "Bishop"

  ' Insert Queen
  Range("D1").Value = "Queen"

  ' Insert King
  Range("E1").Value = "King"

  ' Using Cells
  ' ---------------------------------------

  ' Insert Pawns
  Cells(7, 1).Value = "Pawn"
  Cells(7, 2).Value = "Pawn"
  Cells(7, 3).Value = "Pawn"
  Cells(7, 4).Value = "Pawn"
  Cells(7, 5).Value = "Pawn"
  Cells(7, 6).Value = "Pawn"
  Cells(7, 7).Value = "Pawn"
  Cells(7, 8).Value = "Pawn"

  ' Insert Rooks
  Cells(8, 1).Value = "Rook"
  Cells(8, 8).Value = "Rook"

  ' Insert Knights
  Cells(8, 2).Value = "Knight"
  Cells(8, 7).Value = "Knight"

  ' Insert Bishops
  Cells(8, 3).Value = "Bishop"
  Cells(8, 6).Value = "Bishop"

  ' Insert Queen
  Cells(8, 4).Value = "Queen"

  ' Insert King
  Cells(8, 5).Value = "King"

End Sub
