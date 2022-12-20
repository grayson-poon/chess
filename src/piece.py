class Piece:
	def __init__(self, name: str, color: str) -> None:
		self._name = name
		self._color = color
		self._out = False

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

