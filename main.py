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
    def within_reach(self,x,y):
        if self.color == 'b':
            x, y = x*-1, y*-1
        
        if x==0 and y == 1:
            return ('move')
        elif x == 1 and abs(y)==1 :
            return ('take')
        else :
            return False
    


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
        return (f'{self.name} playing {self.color_repr}')
    
    def set_piece(self, positions, piece):
        try:
            piece.color  = self.color
        except ValueError:
            raise ValueError(f'Piece {piece} has no color attribute')

        for position in positions:
            self.pieces[position]= piece
    
    def his_position(self,position):
        return position in self.pieces.keys()
    
def vector(board, from_position, to_position):
    try:
        type(board) == Board
    except TypeError:
        return (0,0)

    from_file, from_rank = board._parse_position(from_position)
    to_file, to_rank = board._parse_position(to_position)
        #compute vector as Tuple(number of field in forward direction, sideways direction)
    files, _ = board._board_plan()
    v_sideways = files.find(to_file)-files.find(from_file)
    v_ahead = to_rank - from_rank
   
    return v_ahead,v_sideways




def main():        

    size = 3
    b=Board(size)
    p_b = Pawn('b')
    p_w = Pawn('w')

    player_A = Player('Hugo','b')
    player_B = Player('Elvis','w')

    player_A.set_piece(['a3','b3','c3'], p_b)

    player_B.set_piece(['a1','b1','c1'], p_w)
    players = [player_A,player_B]

    for position,piece in player_A.pieces.items():
        b.place_item(piece, position)

    for position,piece in player_B.pieces.items():
        b.place_item(piece, position)


    turn = 1
    b.show()
    while True:
        playing_player = turn%2
        opposing_player = (playing_player+1)%2
        
        try: # taking move to do
            from_position, to_position =  input(f'whats your next move {players[playing_player]}? ').split(',')
            from_position, to_position = from_position.strip(), to_position.strip() # stripped of unneccessary blanks
        except ValueError:
            break
                
        move_vector = vector(b, from_position, to_position)

        if move_vector == (0,0):
            print ('move somewhere else')
            continue

        if not players[playing_player].his_position(from_position):
            print (f'You do not have piece on position {from_position}')
            continue

        moving_piece = b.get_item(from_position)

        if not b.is_free(to_position):  
            # if destination is taken by friendly piece
            if b.get_item(to_position).color == moving_piece.color:
                print('you fool, there is your piece!! Again')
                continue # turn is not completed 
            
            print (f'Player {players[opposing_player]} looses piece on {to_position}') # little info
            del players[opposing_player].pieces[to_position] # deletion from the players set

        del players[playing_player].pieces[from_position]
        players[playing_player].pieces[to_position] = moving_piece

        b.move(from_position, to_position)

        b.show()
        turn += 1
        print(player_A.name, player_A.pieces)
        print(player_B.name, player_B.pieces)


if __name__ == '__main__':
    main()
        



            

       


