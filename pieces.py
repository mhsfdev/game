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

        return self._color == piece.color
    
    def is_black(self):
        return self._color=='b'
    
    def is_white(self):
        return self._color=='w'

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
    """
    future refactiorin / use dictionary to set legal moves and claim legal if in values and return key to indicate type of move
    """

    
    def within_reach(self,move_vector):
        """
        returns False if vector of movement is out of reach for the Piece
        Args:
            vector of the move 
        """
        ahead,sideways = move_vector
        if self.is_black():
            ahead, sideways = ahead * -1, sideways * -1 # for black player playing down the vector is turned by 180 degrees
        
        if ahead == 1 and sideways == 0:
            return ('move')
        elif ahead == 1 and abs(sideways) == 1 :
            return ('take')
        else :
            return False
    
    def legal_moves(self): 
        if self.is_white():
            return {
                'move' : [(1,0)], 
                'take' : [(1,-1),(1,1)]

            }
            
        else:
             return {
                'move' : [(-1,0)], 
                'take' : [(-1,1),(-1,-1)]

            }