from unittest import TestCase
from rook import Rook
from piece import Colour
from pawn import Pawn

class RookTestSuite(TestCase):

    def test_rook_moves(self):
        rook1 = Rook(Colour.WHITE)
        pawn1 = Pawn(Colour.WHITE, (0, 1))
        self.assertEquals(set(rook1.list_moves([pawn1])),
                          set(zip(range(1, 8), [0]*8)))
