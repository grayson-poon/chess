import sys
sys.path.append("../")
sys.path.append("./pieces")

from spot import Spot
from pieces.piece import Piece
from pieces.pawn import Pawn
from constants import colors, piece_names

class Board:
  def __init__(self) -> None:
    # create a Spot class
      self._board = [[None for i in range(0, 8)] for j in range(0, 8)]

  @property
  def board(self) -> list[list[Spot | None]]:
    return self._board

  def createBoard(self) -> None:
    self.resetBoard()

  def resetBoard(self) -> None:
    # create rooks and set on board

    # ------- REPLACE PIECE WITH ACTUAL child class pieces
    self._board[0][0] = Spot(0, 0, Piece(piece_names.ROOK, colors.BLACK))
    self._board[0][7] = Spot(0, 7, Piece(piece_names.ROOK, colors.BLACK))
    self._board[7][0] = Spot(7, 0, Piece(piece_names.ROOK, colors.WHITE))
    self._board[7][7] = Spot(7, 7, Piece(piece_names.ROOK, colors.WHITE))

    # create knights and set on board
    self._board[0][1] = Spot(0, 1, Piece(piece_names.KNIGHT, colors.BLACK))
    self._board[0][6] = Spot(0, 6, Piece(piece_names.KNIGHT, colors.BLACK))
    self._board[7][1] = Spot(7, 1, Piece(piece_names.KNIGHT, colors.WHITE))
    self._board[7][6] = Spot(7, 6, Piece(piece_names.KNIGHT, colors.WHITE))

    # create bishops and set on board
    self._board[0][2] = Spot(0, 2, Piece(piece_names.BISHOP, colors.BLACK))
    self._board[0][5] = Spot(0, 5, Piece(piece_names.BISHOP, colors.BLACK))
    self._board[7][2] = Spot(7, 2, Piece(piece_names.BISHOP, colors.WHITE))
    self._board[7][5] = Spot(7, 5, Piece(piece_names.BISHOP, colors.WHITE))

    # create queens and set on board
    self._board[0][3] = Spot(0, 3, Piece(piece_names.QUEEN, colors.BLACK))
    self._board[7][3] = Spot(7, 3, Piece(piece_names.QUEEN, colors.BLACK))

    # create kings and set on board
    self._board[0][4] = Spot(0, 4, Piece(piece_names.KING, colors.BLACK))
    self._board[7][4] = Spot(7, 3, Piece(piece_names.KING, colors.WHITE))

    # create pawns and set on board
    for i in range(0, 8):
      self._board[1][i] = Spot(1, i, Pawn(piece_names.PAWN, colors.BLACK))
      self._board[6][i] = Spot(6, i, Pawn(piece_names.PAWN, colors.WHITE))
    
    # create empty spots and set on board
    for y in range(2, 6):
      for x in range(0, 8):
        self._board[y][x] = Spot(y, x, None)
