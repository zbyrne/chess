from unittest import TestCase
from bishop import Bishop
from piece import Colour
from pawn import Pawn

class BishopTestSuite(TestCase):

    def test_bishop_moves(self):
        bishop1 = Bishop(Colour.WHITE)
        pawn1 = Pawn(Colour.WHITE, (2, 2))
        self.assertEquals(set(bishop1.list_moves([pawn1])),
                          set([(1, 1)]))

    def test_bishop_attacks(self):
        bishop1 = Bishop(Colour.WHITE, (3, 3))
        pawn1 = Pawn(Colour.WHITE, (2, 2))
        pawn2 = Pawn(Colour.BLACK, (4, 4))
        pawn3 = Pawn(Colour.BLACK, (5, 5))
        self.assertEquals(set(bishop1.list_attacks([pawn1, pawn2, pawn3])),
                          set([((4, 4))]))
