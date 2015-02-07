from piece import Colour
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook

STARTING_BOARD = (Pawn(Colour.WHITE, (0, 1)),
                  Pawn(Colour.WHITE, (1, 1)),
                  Pawn(Colour.WHITE, (2, 1)),
                  Pawn(Colour.WHITE, (3, 1)),
                  Pawn(Colour.WHITE, (4, 1)),
                  Pawn(Colour.WHITE, (5, 1)),
                  Pawn(Colour.WHITE, (6, 1)),
                  Pawn(Colour.WHITE, (7, 1)),
                  Rook(Colour.WHITE, (0, 0)),
                  Rook(Colour.WHITE, (7, 0)),
                  Knight(Colour.WHITE, (1, 0)),
                  Knight(Colour.WHITE, (6, 0)),
                  Bishop(Colour.WHITE, (2, 0)),
                  Bishop(Colour.WHITE, (5, 0)),
                  Queen(Colour.WHITE, (3, 0)),
                  King(Colour.WHITE, (4, 0)),
                  Pawn(Colour.BLACK, (0, 6)),
                  Pawn(Colour.BLACK, (1, 6)),
                  Pawn(Colour.BLACK, (2, 6)),
                  Pawn(Colour.BLACK, (3, 6)),
                  Pawn(Colour.BLACK, (4, 6)),
                  Pawn(Colour.BLACK, (5, 6)),
                  Pawn(Colour.BLACK, (6, 6)),
                  Pawn(Colour.BLACK, (7, 6)),
                  Rook(Colour.BLACK, (0, 7)),
                  Rook(Colour.BLACK, (7, 7)),
                  Knight(Colour.BLACK, (1, 7)),
                  Knight(Colour.BLACK, (6, 7)),
                  Bishop(Colour.BLACK, (2, 7)),
                  Bishop(Colour.BLACK, (5, 7)),
                  Queen(Colour.BLACK, (3, 7)),
                  King(Colour.BLACK, (4, 7)))


class GameTree(object):
    def __init__(self, pieces, colour):
        self.pieces = list(pieces)
        self.colour = colour
        self.children = []

    def generate(self, generations=1):
        next_gen_colour = (Colour.WHITE
                         if self.colour == Colour.BLACK
                         else Colour.BLACK)
        candidates = [p for p in self.pieces if p.colour == self.colour]
        for cand in candidates:
            board = self.pieces[:]
            board.remove(cand)
            for move in cand.list_moves(board):
                clone = cand.clone()
                clone.position = move
                new_board = board[:]
                new_board.append(clone)
                self.children.append(GameTree(new_board, next_gen_colour))
            for attack in cand.list_attacks(board):
                clone = cand.clone()
                clone.position = attack
                new_board = board[:]
                new_board.append(clone)
                casualty = [x for x in board if x.position == attack][0]
                new_board.remove(casualty)
                self.children.append(GameTree(new_board, next_gen_colour))
        if generations <= 1:
            return
        for child in self.children:
            child.generate(generations=generations-1)
