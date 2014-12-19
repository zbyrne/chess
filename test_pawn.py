from unittest import TestCase
from pawn import Pawn
from piece import Colour


class PawnTestSuite(TestCase):

    def test_pawn_moves(self):
        pawn1 = Pawn(Colour.WHITE, (0, 0))
        pawn2 = Pawn(Colour.BLACK, (0, 1))
        pawn3 = Pawn(Colour.BLACK, (0, 0))
        self.assertEquals(pawn1.list_moves([]), [(0, 1)])
        self.assertEquals(pawn1.list_moves([pawn2]), [])
        self.assertEquals(pawn3.list_moves([]), [])

    def test_pawn_attacks(self):
        pawn1 = Pawn(Colour.WHITE, (0, 0))
        pawn2 = Pawn(Colour.BLACK, (1, 1))
        self.assertEquals(pawn1.list_attacks([pawn2]), [(1, 1)])
