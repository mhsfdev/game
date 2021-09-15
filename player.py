import random

class Player:
    """
    Player collects data on player
    creates dictionary of posiitons(key) and pieces(values) where pieces of the game are kept and evaluated for game result /valid moves, existence of pieces to be played with
    args :
        name:name of the Player
        color :black or white
    """
    def __init__(self, name, color,human = True ):
        
        self.name = name
        self.pieces = {}
        self._is_human = human
        """ enables to work with dictionary methods to retrieve Piece into gaming
        """
        if color not in ['b','w']:
            raise ValueError(f'Color {color} is not valid')
        else:
            self._color = color
            
            if self._color.lower() == 'b':
                self._color_repr =  'X'
            elif self._color.lower() =='w':
                self._color_repr =  'O'            
    
    
    @property
    def is_human(self):
        return self._is_human == True
    @property
    def is_CPU(self):
        return self._is_human == False
    
    @property
    def color(self):
        return self._color

    @property
    def positions(self):
        return list(self.pieces.keys())
    

    def __repr__(self):
        return(f'Player("{self.name}", human = {self.is_human}, color={self.color})')
    def __str__(self):
        return (f'{self.name} ({self._color_repr})')
    

    def set_piece(self, positions, piece):
        try:
            piece.color  = self.color
        except ValueError:
            raise ValueError(f'Piece {piece} has no color attribute')

        for position in positions:
            self.pieces[position]= piece
    
    def his_position(self,position):
        
        return position in self.pieces.keys()
    
    def make_move(self, board):
        if self.is_human: #available only for CPU player
            raise TypeError('this function is availabe only for CPU players')
        try:
            legal_moves = board.legal_moves(*self.positions)
        except ValueError:
            return None
        
        return self._random_move(legal_moves) 
    
    def _random_move(self,available_moves) -> tuple :
        """
        from available moves structured as dictionary when key is position and value is list availble moves in tuples 
        """

        try:
            random_position = random.choice(list(available_moves.keys()))
            return random.choice(available_moves[random_position])
        except TypeError or ValueError:
            raise TypeError('Not valid Structure')



        

        


        
    
