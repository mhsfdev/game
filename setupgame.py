from board import Board
from pieces import Pawn
from player import Player



size = 5
b = Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

player_A = Player('Hugo', 'b')
player_B = Player('Elvis', 'w')

player_A.set_piece(['a3', 'b3', 'c3'], p_b)

player_B.set_piece(['a1', 'b2', 'c1'], p_w)
players = [player_A, player_B]

for position, piece in player_A.pieces.items():
    b.place_item(piece, position)

for position, piece in player_B.pieces.items():
    b.place_item(piece, position)

turn = 1
b.show()