
import random

def random_move(board,moves):
    
    
    random_position = random.choice(list(moves.keys()))
    
    
    available_legal_moves = moves[random_position]
    return random.choice(available_legal_moves)

board = 'Board'

legal_moves={
    'b2':[('b2','B1'),('b2','A1')],
    'c2':[('c2','C1')],
    'a2':[('a2','a1'),('a2','b1'),('a2','c1')]
    
}

print(random_move(board, legal_moves))

