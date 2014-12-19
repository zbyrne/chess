from piece import Piece, Colour


class Pawn(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Pawn, self).__init__(colour, position)
        self._moves = [(0, 1)]
        self._attacks = [(-1, 1), (1, 1)]

