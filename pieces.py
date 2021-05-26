class Piece:
    def __init__(self, color = 'b'):
        
        if color.lower() not in 'bw':
            raise ValueError(f'Color {color} is not supported')
        self.color = color
        
    
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
    def within_reach(self,ahead,sideways):
        """
        returns False if vector of movement is out of reach for the Piece
        Args:
            vector of the move 
        """
        if self.color == 'b':
            ahead, sideways = ahead*-1, sideways*-1 # for black player playing down the vector is turned by 180 degrees
        
        if ahead== 1 and sideways == 0:
            return ('move')
        elif ahead == 1 and abs(sideways)==1 :
            return ('take')
        else :
            return False
    