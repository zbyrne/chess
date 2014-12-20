from piece import Piece


class Bishop(Piece):
    def __init__(self, colour, position=(0, 0)):
        super(Bishop, self).__init__(colour, position)
        self._moves = [
            (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3),
            (-2, -2), (-1, -1),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-7, 7), (-6, 6), (-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)]
