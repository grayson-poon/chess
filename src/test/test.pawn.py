import sys
sys.path.append("../")
sys.path.append("../pieces")
sys.path.append("../constants")

from board import Board
from spot import Spot
from pieces.pawn import Pawn
from constants import colors

print("---------------------------BLACK PAWN TESTS---------------------------")

b = Board()
b.resetBoard()

# select Pawn spots
spot1: Spot = b.board[1][3]
spot2: Spot = b.board[1][1]
spot3: Spot = b.board[1][0]
spot4: Spot = b.board[1][7]

# BLACK pawn objects
pawn1: Pawn = spot1.piece
pawn2: Pawn = spot2.piece
pawn3: Pawn = spot3.piece
pawn4: Pawn = spot4.piece

# determine potential spots for pawn to move
pawn1Spots: list[Spot] = pawn1.findPotentialSpots(b.board[1][3], b.board, 1) # [2, 3], [3, 3]
pawn2Spots: list[Spot] = pawn2.findPotentialSpots(b.board[1][1], b.board, 1) # [2, 1], [3, 1]
pawn3Spots: list[Spot] = pawn3.findPotentialSpots(b.board[1][0], b.board, 1) # [2, 0], [3, 0]
pawn4Spots: list[Spot] = pawn4.findPotentialSpots(b.board[1][7], b.board, 1) # [2, 7], [3, 7]

print("PAWN1: ", f'{len(pawn1Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn1Spots])
print("PAWN2: ", f'{len(pawn2Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn2Spots])
print("PAWN3: ", f'{len(pawn3Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn3Spots])
print("PAWN4: ", f'{len(pawn4Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn4Spots])

print("--------------------------eat other pawns------------------------------")
b.resetBoard()

# reassign board[2][4] and [2][2] to white Pawns -> test if pawns will eat other pieces
b.board[2][2].piece = Pawn("", colors.WHITE)
b.board[2][4].piece = Pawn("", colors.WHITE)

pawn1Spots: list[Spot] = pawn1.findPotentialSpots(b.board[1][3], b.board, 1)
pawn2Spots: list[Spot] = pawn2.findPotentialSpots(b.board[1][1], b.board, 1)

print("PAWN1: ", f'{len(pawn1Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn1Spots]) # [2, 3], [3, 3], [2, 4], [2, 2]
print("PAWN2: ", f'{len(pawn2Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn2Spots]) # [2, 1], [3, 1], [2, 2]

print("---------------------------cannot move--------------------------------")

# reassign board[2][0] and [2][7] to white pawns -> testing that the pawns at [1][0] and [1][7] cannot move at all
b.board[2][0].piece = Pawn("", colors.WHITE)
b.board[2][7].piece = Pawn("", colors.WHITE)

pawn3Spots: list[Spot] = pawn3.findPotentialSpots(b.board[1][0], b.board, 1)
pawn4Spots: list[Spot] = pawn4.findPotentialSpots(b.board[1][7], b.board, 1)

print("PAWN3: ", f'{len(pawn3Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn3Spots]) # []
print("PAWN4: ", f'{len(pawn4Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn4Spots]) # []

print("---------------------------WHITE PAWN TESTS---------------------------")
b.resetBoard()

# select Pawn spots
spot1: Spot = b.board[6][3]
spot2: Spot = b.board[6][1]
spot3: Spot = b.board[6][0]
spot4: Spot = b.board[6][7]

# WHITE pawn objects
pawn1: Pawn = spot1.piece
pawn2: Pawn = spot2.piece
pawn3: Pawn = spot3.piece
pawn4: Pawn = spot4.piece

# determine potential spots for pawn to move
pawn1Spots: list[Spot] = pawn1.findPotentialSpots(b.board[6][3], b.board, 1) # [5, 3], [4, 3]
pawn2Spots: list[Spot] = pawn2.findPotentialSpots(b.board[6][1], b.board, 1) # [5, 1], [4, 1]
pawn3Spots: list[Spot] = pawn3.findPotentialSpots(b.board[6][0], b.board, 1) # [5, 0], [4, 0]
pawn4Spots: list[Spot] = pawn4.findPotentialSpots(b.board[6][7], b.board, 1) # [5, 7], [4, 7]

print("PAWN1: ", f'{len(pawn1Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn1Spots])
print("PAWN2: ", f'{len(pawn2Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn2Spots])
print("PAWN3: ", f'{len(pawn3Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn3Spots])
print("PAWN4: ", f'{len(pawn4Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn4Spots])

print("--------------------------eat other pawns------------------------------")
b.resetBoard()

# reassign board[5][4] and [5][2] to black Pawns -> test if pawns will eat other pieces
b.board[5][2].piece = Pawn("", colors.BLACK)
b.board[5][4].piece = Pawn("", colors.BLACK)

pawn1Spots: list[Spot] = pawn1.findPotentialSpots(b.board[6][3], b.board, 1)
pawn2Spots: list[Spot] = pawn2.findPotentialSpots(b.board[6][1], b.board, 1)

print("PAWN1: ", f'{len(pawn1Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn1Spots]) # [5, 3], [4, 3], [5, 4], [5, 2]
print("PAWN2: ", f'{len(pawn2Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn2Spots]) # [5, 1], [4, 1], [5, 2]

print("---------------------------cannot move--------------------------------")

# reassign board[5][0] and [5][7] to black pawns -> testing that the pawns at [6][0] and [6][7] cannot move at all
b.board[5][0].piece = Pawn("", colors.BLACK)
b.board[5][7].piece = Pawn("", colors.BLACK)

pawn3Spots: list[Spot] = pawn3.findPotentialSpots(b.board[6][0], b.board, 1)
pawn4Spots: list[Spot] = pawn4.findPotentialSpots(b.board[6][7], b.board, 1)

print("PAWN3: ", f'{len(pawn3Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn3Spots]) # []
print("PAWN4: ", f'{len(pawn4Spots)} potential moves to', [[spot.y, spot.x] for spot in pawn4Spots]) # []
