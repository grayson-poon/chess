import sys
sys.path.append("../")

from piece import Piece
from spot import Spot

# Knight moves:
# 	* Always moves in (x +/- 2 and y +/-1) or (x +/- 1 and y +/- 2)
# 	* Can eat a Piece in a Spot occupied by a different color
# 	* Cannot move to a Spot occupied by the same color

class Knight(Piece):
	def __init__(self, name: str, color: str) -> None:
		super().__init__(name, color)
	
	def canMove(self, start: Spot, end: Spot) -> bool:
		deltaY = abs(start.y - end.y)
		deltaX = abs(start.x - end.x)

		# Spot is valid as long as the Knight does not eat its own color
		if end.piece.color == self.color:
			return False
		
		# change in Y x change in X should always be 2
		return (deltaY * deltaX) == 2

	def findPotentialSpots(self, start: Spot, board: list[list[Spot]]) -> list[Spot]:
		potential_spots: list[Spot] = []

		potential_coords: list[list[int]] = [
			# translate y by 2 and x by 1
			[start.y + 2, start.x + 1],
			[start.y + 2, start.x - 1],
			[start.y - 2, start.x + 1],
			[start.y - 2, start.x - 1],
			# translate y by 1 and x by 2
			[start.y + 1, start.x + 2],
			[start.y + 1, start.x - 2],
			[start.y - 1, start.x + 2],
			[start.y - 1, start.x - 2],
		]

		'''
MAYBE DEFER ITERATION THROUGH potential_coords TO BE AN INSTANCE METHOD, SINCE
THIS SECTION OF CODE WILL PROBABLY BE THE SAME FOR ALL PIECES
		'''
		# return self.filterCoords(start, board, potential_coords)

		for [y, x] in potential_coords:
			if self.willBeInbounds(y, x):
				end: Spot = board[y][x]

				if self.canMove(start, end):
					potential_spots.append(end)
		return potential_spots