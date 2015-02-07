from unittest import TestCase
from king import King
from piece import Colour
from pawn import Pawn

class KingTestSuite(TestCase):

    def test_king_moves(self):
        king1 = King(Colour.WHITE, (4, 4))
        pawn1 = Pawn(Colour.WHITE, (4, 5))
        pawn2 = Pawn(Colour.WHITE, (4, 3))
        pawn3 = Pawn(Colour.WHITE, (3, 3))
        pawn4 = Pawn(Colour.WHITE, (5, 5))
        self.assertEquals(set(king1.list_moves([pawn1, pawn2, pawn3, pawn4])),
                          set([(3, 5), (5, 3), (5, 4), (3, 4)]))

    def test_king_attacks(self):
        king1 = King(Colour.WHITE, (4, 4))
        pawn1 = Pawn(Colour.BLACK, (4, 5))
        pawn2 = Pawn(Colour.BLACK, (4, 6))
        self.assertEquals(set(king1.list_attacks([pawn1, pawn2])),
                          set([(4, 5)]))
