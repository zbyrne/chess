from unittest import TestCase
from gameTree import GameTree
from piece import Colour
from queen import Queen
from pawn import Pawn
from king import King

class GameTreeTestSuite(TestCase):

    def test_game_progression(self):
        board = (Pawn(Colour.WHITE, (0, 0)), Pawn(Colour.BLACK, (7, 7)))
        for p in board:
            p._moved = True
        gt = GameTree(board, Colour.WHITE)
        gt.generate(2)
        self.assertEquals(len(gt.children), 1)
        for p in gt.children[0].pieces:
            if p.colour == Colour.WHITE:
                self.assertEquals(p.position, (0, 1))
            else:
                self.assertEquals(p.position, (7, 7))
        self.assertEquals(len(gt.children[0].children), 1)
        for p in gt.children[0].children[0].pieces:
            if p.colour == Colour.WHITE:
                self.assertEquals(p.position, (0, 1))
            else:
                self.assertEquals(p.position, (7, 6))
