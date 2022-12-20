from piece import Piece

class Pawn(Piece):
	def __init__(self, name: str, color: str) -> None:
		super().__init__(name, color)