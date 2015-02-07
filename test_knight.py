from unittest import TestCase
from knight import Knight
from piece import Colour
from pawn import Pawn

class KnightTestSuite(TestCase):

    def test_knight_moves(self):
        knight1 = Knight(Colour.WHITE, (4, 4))
        pawn1 = Pawn(Colour.WHITE, (3, 6))
        self.assertEquals(set(knight1.list_moves([pawn1])),
                          set([(5, 6), (3, 2), (6, 3), (2, 3),
                               (2, 5), (5, 2), (6, 5)]))

    def test_knight_attacks(self):
        knight1 = Knight(Colour.WHITE, (4, 4))
        pawn1 = Pawn(Colour.WHITE, (3, 6))
        pawn2 = Pawn(Colour.BLACK, (3, 2))
        pawn3 = Pawn(Colour.BLACK, (3, 3))
        self.assertEquals(set(knight1.list_attacks([pawn1, pawn2, pawn3])),
                              set([(3, 2)]))
