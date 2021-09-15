
from board import *
from pieces import *
from player import *
from board import *


board = PawnGameBoard()

expected_legal_moves={
    'b2':[('b2','B1'),('b2','A1')],
    'c2':[('c2','C1')],
    'a2':[('a2','a1'),('a2','b1'),('a2','c1')]
    
}
wpawn = Pawn('w')
bpawn = Pawn('b')

player = Player('Hugo',color='b', human=True)
positions =['a2','b2','c2']
player.set_piece(positions, bpawn)
board.setup_pieces(positions, bpawn)
board.setup_pieces(['b1'],wpawn)
board.show()
print(player,type(player.pieces.keys()))
print(player.pieces.keys())

print(type(player.positions), player.positions)

print(board.legal_moves(*player.positions))