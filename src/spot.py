from piece import Piece

class Spot:
  def __init__(self, x: int, y: int, piece: Piece | None) -> None:
    self._x = x
    self._y = y
    self._piece = piece

  @property
  def x(self) -> int:
    return self._x

  @property
  def y(self) -> int:
    return self._y

  @property
  def piece(self) -> Piece:
    return self._piece
  
  @piece.setter
  def piece(self, piece: Piece) -> None:
    self._piece = piece

