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
    def within_reach(self,x,y):
        """
        returns False if vector of movement is out of reach for the Piece
        Args:
            vector of the move 
        """
        if self.color == 'b':
            x, y = x*-1, y*-1 # for black player playing down the vector is turned by 180 degrees
        
        if x==0 and y == 1:
            return ('move')
        elif x == 1 and abs(y)==1 :
            return ('take')
        else :
            return False
    