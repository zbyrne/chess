from piece import Piece


class Knight(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Knight, self).__init__(colour, position)

    @property
    def _moves(self):
        return [(-1, -2), (-1, 2), (1, -2), (1, 2),
                (-2, -1), (-2, 1), (2, -1), (2, 1)]

    @property
    def _attacks(self):
        return [(-1, -2), (-1, 2), (1, -2), (1, 2),
                (-2, -1), (-2, 1), (2, -1), (2, 1)]

    def _blocks_move(self, piece, move):
        return False
