from unittest import TestCase
from piece import Piece, Colour


class PieceTestSuite(TestCase):

    def test_piece_position(self):
        piece = Piece(Colour.WHITE)
        self.assertEqual(piece.position, (0, 0))
        piece.position = (1, 1)
        self.assertEqual(piece.position, (1, 1))
        with self.assertRaises(TypeError):
            piece.position = 'spam'
        with self.assertRaises(ValueError):
            piece.position = (-1, 8)
        with self.assertRaises(ValueError):
            piece2 = Piece(Colour.WHITE, (-1, 8))

    def test_piece_colour(self):
        piece = Piece(Colour.WHITE)
        self.assertEqual(piece.colour, Colour.WHITE)
        with self.assertRaises(ValueError):
            piece2 = Piece('spam')

    def test_piece_moves(self):
        piece = Piece(Colour.WHITE)
        self.assertEqual(piece.list_moves([]), [])

    def test_piece_attacks(self):
        piece = Piece(Colour.WHITE)
        self.assertEqual(piece.list_attacks([]), [])
