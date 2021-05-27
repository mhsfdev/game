class Piece:
    def __init__(self, color = 'b'):
        
        
        self._color = color
        
    
    def __repr__(self):
        if self._color.lower() == 'b':
            return 'X'
        elif self._color.lower() =='w':
            return 'O'
    def same_color(self, piece):
        try :
            piece.color
        except AttributeError('not valid piece'):
            return False

        return self.color == piece.color
    
    def is_black(self):
        return self._color=='b'
    
    def is_white(self):
        return self._same_clorocolor=='w'

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        if color.lower() not in 'bw':
            self._color = 'b'
        else:
            self._color = color


      

class Pawn(Piece):
    def within_reach(self,ahead,sideways):
        """
        returns False if vector of movement is out of reach for the Piece
        Args:
            vector of the move 
        """
        if self.is_black:
            ahead, sideways = ahead*-1, sideways*-1 # for black player playing down the vector is turned by 180 degrees
        
        if ahead== 1 and sideways == 0:
            return ('move')
        elif ahead == 1 and abs(sideways)==1 :
            return ('take')
        else :
            return False
    