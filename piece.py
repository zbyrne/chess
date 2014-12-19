class Colour(object):
    WHITE = 'white'
    BLACK = 'black'


def position_on_board(position):
    board = range(8)
    return all(x in board for x in position)


class Piece(object):
    def __init__(self, colour, position=(0, 0)):
        if not position_on_board(position):
            raise ValueError, 'position must be on the board'
        self._position = position
        if colour not in (Colour.WHITE, Colour.BLACK):
            raise ValueError, 'What game are you playing?'
        self._colour = colour
        self._moves = []
        self._attacks = []

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError, 'position must be a tuple, not %s' % type(value)
        if not position_on_board(value):
            raise ValueError, 'position must be on the board'
        self._position = value

    @property
    def colour(self):
        return self._colour

    def list_moves(self, pieces):
        moves = []
        for move in self._moves:
            end_pos = self._add_move(move)
            if not position_on_board(end_pos):
                continue
            if not pieces:
                moves.append(end_pos)
            for piece in pieces:
                if (piece.position != end_pos and
                    not self._blocks_move(piece, end_pos)):
                    moves.append(end_pos)
        return moves

    def list_attacks(self, pieces):
        attacks = []
        for attack in self._attacks:
            att_pos = self._add_move(attack)
            if not position_on_board(att_pos):
                continue
            for piece in pieces:
                if (piece.position == att_pos and
                    piece.colour != self._colour):
                    attacks.append(att_pos)
        return attacks

    def _add_move(self, move):
        x = move[0]
        y = move[1] if self._colour == Colour.WHITE else -move[1]
        return (self.position[0] + x, self.position[1] + y)

    def _blocks_move(self, piece, move):
        xdiff = move[0] - self._position[0]
        if xdiff > 0:
            xstep = 1
        elif xdiff < 0:
            xstep = -1
        else:
            xstep = 0
        ydiff = move[1] - self._position[1]
        if ydiff > 0:
            ystep = 1
        elif ydiff < 0:
            ystep = -1
        else:
            ystep = 0
        line = []
        point = (self.position[0] + xstep, self.position[1] + ystep)
        while point != move:
            line.append(point)
            point = (point[0] + xstep, point[1] + ystep)
        return piece.position in line