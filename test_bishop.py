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
