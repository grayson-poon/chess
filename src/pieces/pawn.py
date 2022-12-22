# # allow code to be compiled despite circular import due to type checking
# from __future__ import annotations

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from board import Board

import sys
sys.path.append("../")

from piece import Piece
from spot import Spot
from constants import colors

# Pawn moves:

# Moves forward by one Spot each time:
#     * Black -> board[y + 1][x = constant]
#     * White -> board[y - 1][x = constant]

# Moves diagonally to eat opposite color piece only:
#     * Black -> board[y + 1][x +- 1]
#     * White -> board[y - 1][x +- 1]

# Has the option to move 2 spaces forward if it is that pawn's first move
#     * Black -> board[y + 2][x = constant]
#     * White -> board[y - 2][x = constant]

# Cannot move directly forward if there is any piece in front of it

# If Pawn reaches the opposite end of the board, Player has the option to
# replace the Pawn with any of their previously eaten pieces

class Pawn(Piece):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, color)

    def canMove(self, start: Spot, end: Spot) -> bool:
        # 0 change in x position = straight forward move
        # change in x of 1 = eating another piece
        deltaX = abs(start.x - end.x)

        if deltaX == 0:
            # if end spot has a Piece occupying the space, cannot move
            if end.piece is not None:
                return False
        else:
            # cannot eat an empty Spot or eat a Piece of the same color
            if end.piece is None or end.piece.color == self.color:
                return False
        return True


    def findPotentialSpots(self, start: Spot, board: list[list[Spot]], direction: int = 1) -> list[Spot]:
        # switch y-direction when white to ensure Pawn moves in the correct direction
        if self.color == colors.WHITE:
            direction = -1
        
        potential_spots: list[Spot] = []

        # all potential coordinate adjustments for Pawns
        potential_coords: list[list[int]] = [
            [start.y + (1 * direction), start.x],
            [start.y + (2 * direction), start.x],
            [start.y + (1 * direction), start.x + 1],
            [start.y + (1 * direction), start.x - 1]
        ]

        # iterate through potential coordinates and determine if Pawn can occupy the spot
        for [y, x] in potential_coords:
            # cannot move two spots forward if unable to move one spot forward
            if abs(start.y - y) == 2 and len(potential_spots) == 0:
                continue

            if self.willBeInbounds(y, x):
                end: Spot = board[y][x]
                
                if self.canMove(start, end):
                    potential_spots.append(end)
        return potential_spots
