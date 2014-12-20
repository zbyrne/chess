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

    def test_rook_attacks(self):
        rook1 = Rook(Colour.WHITE)
        pawn1 = Pawn(Colour.WHITE, (0, 1))
        pawn2 = Pawn(Colour.BLACK, (1, 0))
        pawn3 = Pawn(Colour.BLACK, (3, 0))
        self.assertEquals(set(rook1.list_attacks([pawn1, pawn2, pawn3])),
                          set([((1, 0))]))
