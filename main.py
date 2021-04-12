from board import Board

class Piece:
    def __init__(self, color = 'b'):
        self.color = color
        if color.lower() not in 'bw':
            raise ValueError(f'Color {color} is not supported')
      
        
    
    def __repr__(self):
        if self.color.lower() == 'b':
            return 'X'
        elif self.color.lower() =='w':
            return 'O'

class Pawn(Piece):
    pass
    
        

size = 3
b=Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

for line in reversed(range(1,size+1)):
    print(f'{line}: {b.board[line]}')


 
b.place_item(p_b, 'A1')

b.place_item(p_b, 'C1')
b.place_item(p_w, 'b1')

b.visualize()

print(b.move('b1','c2'))
b.visualize()

            

       


