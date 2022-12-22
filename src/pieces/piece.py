class Piece:
	def __init__(self, name: str, color: str) -> None:
		self._name = name
		self._color = color
		self._out = False
		self._number_of_moves_made = 0
		self._potential_moves = []

	@property
	def name(self) -> str:
		return self._name

	@property
	def color(self) -> str:
		return self._color

	@color.setter
	def color(self, color: str) -> None:
		self._color = color

	@property
	def out(self) -> bool:
		return self._out

	@out.setter
	def out(self, out: bool) -> None:
		self._out = out

	@property
	def number_of_moves_made(self) -> int:
		return self._number_of_moves_made
	
	@number_of_moves_made.setter
	def number_of_moves_made(self, value: int) -> None:
		self._number_of_moves_made = value

	@property
	def potential_moves(self) -> list:
		return self._potential_moves

	def willBeInbounds(self, y: int, x: int) -> bool:
		return x >= 0 and x < 8 and y >= 0 and y < 8
