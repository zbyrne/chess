from piece import Piece


class Queen(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Queen, self).__init__(colour, position)
        self._moves = [
            (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3),
            (-2, -2), (-1, -1),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-7, 7), (-6, 6), (-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)]
