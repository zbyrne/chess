from piece import Piece


class King(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(King, self).__init__(colour, position)
        self._moves = [(-1, -1), (-1, 1), (1, -1), (1, 1),
                       (-1, 0), (1, 0), (0, -1), (0, 1)]
        self._attacks = [(-1, -1), (-1, 1), (1, -1), (1, 1),
                         (-1, 0), (1, 0), (0, -1), (0, 1)]
