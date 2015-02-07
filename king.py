from piece import Piece


class King(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(King, self).__init__(colour, position)

    @property
    def _moves(self):
        return [(-1, -1), (-1, 1), (1, -1), (1, 1),
                (-1, 0), (1, 0), (0, -1), (0, 1)]

    @property
    def _attacks(self):
        return [(-1, -1), (-1, 1), (1, -1), (1, 1),
                (-1, 0), (1, 0), (0, -1), (0, 1)]
