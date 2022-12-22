from spot import Spot
from pieces.piece import Piece

class Move:
    def __init__(self, start: Spot, end: Spot) -> None:
        self._start = start
        self._end = end
        self._moved_piece = start.piece
    
    @property
    def start(self) -> Spot:
        return self._start
    
    @property
    def end(self) -> Spot:
        return self._end

    @property
    def moved_piece(self) -> Piece:
        return self._moved_piece
