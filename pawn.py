from piece import Piece, Colour


class Pawn(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Pawn, self).__init__(colour, position)

    @property
    def _moves(self):
        if not self._moved:
            return [(0, 1), (0, 2)]
        return [(0, 1)]

    @property
    def _attacks(self):
        return [(-1, 1), (1, 1)]
