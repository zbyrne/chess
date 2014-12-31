from unittest import TestCase
from queen import Queen
from piece import Colour
from pawn import Pawn

class QueenTestSuite(TestCase):

    def test_queen_moves(self):
        queen1 = Queen(Colour.WHITE, (3, 3))
        pawns = [
            Pawn(Colour.WHITE, (1, 1)),
            Pawn(Colour.WHITE, (5, 5)),
            Pawn(Colour.WHITE, (1, 5)),
            Pawn(Colour.WHITE, (5, 1)),
            Pawn(Colour.WHITE, (3, 1)),
            Pawn(Colour.WHITE, (3, 5)),
            Pawn(Colour.WHITE, (1, 3)),
            Pawn(Colour.WHITE, (5, 3))
            ]
        self.assertEquals(set(queen1.list_moves(pawns)),
                          set([(2, 2), (4, 4), (2, 4), (4, 2),
                               (3, 2), (3, 4), (2, 3), (4, 3)]))

    def test_queen_attacks(self):
        queen1 = Queen(Colour.WHITE, (3, 3))
        pawns = [
            Pawn(Colour.WHITE, (1, 1)),
            Pawn(Colour.BLACK, (5, 5)),
            Pawn(Colour.WHITE, (1, 5)),
            Pawn(Colour.BLACK, (5, 1)),
            Pawn(Colour.WHITE, (3, 1)),
            Pawn(Colour.WHITE, (3, 5)),
            Pawn(Colour.BLACK, (1, 3)),
            Pawn(Colour.WHITE, (5, 3))
            ]
        self.assertEquals(set(queen1.list_attacks(pawns)),
                          set([(5, 5), (5, 1), (1, 3)]))
