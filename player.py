class Player:
    """
    Player collects data on player
    creates dictionary of posiitons(key) and pieces(values) where pieces of the game are kept and evaluated for game result /valid moves, existence of pieces to be played with
    args :
        name:name of the Player
        color :black or white
    """
    def __init__(self, name, color):
        self.name = name
        self.pieces = {} 
        """ enables to work with dictionary methods to retrieve Piece into gaming
        """
        if color not in ['b','w']:
            raise ValueError(f'Color {color} is not valid')
        else:
            self.color = color
            
            if self.color.lower() == 'b':
                self.color_repr =  'X'
            elif self.color.lower() =='w':
                self.color_repr =  'O'            
    
    def __repr__(self):
        return(f'Player("{self.name}", color={self.color})')
    def __str__(self):
        return (f'{self.name} ({self.color_repr})')
    
    def set_piece(self, positions, piece):
        try:
            piece.color  = self.color
        except ValueError:
            raise ValueError(f'Piece {piece} has no color attribute')

        for position in positions:
            self.pieces[position]= piece
    
    def his_position(self,position):
        return position in self.pieces.keys()
    
    
