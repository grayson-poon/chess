from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pieces.piece import Piece
    from pieces.pawn import Pawn


class Spot:
  def __init__(self, y: int, x: int, piece: Piece | Pawn | None) -> None:
    self._y = y
    self._x = x
    self._piece = piece

  @property
  def x(self) -> int:
    return self._x

  @property
  def y(self) -> int:
    return self._y

  @property
  def piece(self) -> Piece | Pawn | None:
    return self._piece
  
  @piece.setter
  def piece(self, piece: Piece) -> None:
    self._piece = piece
