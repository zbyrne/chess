from piece import Piece


class Rook(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Rook, self).__init__(colour, position)
        self._moves = [
            (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
