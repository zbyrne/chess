from piece import Piece


class Knight(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Knight, self).__init__(colour, position)
        self._moves = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                       (-2, -1), (-2, 1), (2, -1), (2, 1)]
        self._attacks = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                         (-2, -1), (-2, 1), (2, -1), (2, 1)]

    def _blocks_move(self, piece, move):
        return False
