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
    def same_color(self, piece):
        try :
            piece.color
        except AttributeError('not valid piece'):
            return False

        return self.color == piece.color

        

class Pawn(Piece):
    pass


    
        

size = 3
b=Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

player_A = [[p_b,'a1'],[p_b,'b1'],[p_b,'c1']]
player_B = [[p_w,'a3'],[p_w,'b3'],[p_w,'c3']]


for piece, position in player_A:
    b.place_item(piece, position)

for piece, position in player_B:
    b.place_item(piece, position)

b.visualize()

print(b.move('b1','c2'))
b.visualize()

            

       


