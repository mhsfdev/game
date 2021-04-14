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
class Player:

    def __init__(self, name, color):
        self.name = name
        self.pieces = {} 
        """ enables to work with dictionary methods to retrieve Piece into gaming
        """
        if color not in ['b','w']:
            raise ValueError(f'Color {color} is not valid')
        else:
            self.color = color
    
    def __repr__(self):
        return self.name
    
    def set_piece(self, positions, piece):
        try:
            piece.color  = self.color
        except ValueError:
            raise ValueError(f'Piece {piece} has no color attribute')

        for position in positions:
            self.pieces[position]= piece
    
    




    
        

size = 3
b=Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

player_A = Player('Hugo','b')
player_B = Player('Elvis','w')

player_A.set_piece(['a1','b1','c1'], p_b)

player_B.set_piece(['a3','b3','c3'], p_w)
players = [player_A,player_B]

for position,piece in player_A.pieces.items():
    b.place_item(piece, position)

for position,piece in player_B.pieces.items():
    b.place_item(piece, position)


turn = 1
b.visualize()
while True:
    playing_player = turn%2
    
    try: # taking move to do
        from_position, to_position =  input(f'whats your next move {players[playing_player]}? ').split(',')
    except ValueError:
        break
    from_position, to_position = from_position.strip(), to_position.strip() # stripped of unneccessary blanks
    
    
    if b.is_free(to_position): # if destination is free, move i done, turn is completed
        b.move(from_position, to_position)
        turn +=1
        # make changes in players sets
    else:
        piece_out = b.get_item(to_position) # if destination is taken by friendly piece
        if b.get_item(from_position).color == piece_out.color:
            print('you fool, there is your piece!! Again')
            continue # turn is not completed 

        b.move(from_position, to_position)

    b.visualize()
    print(player_A)
    print(player_B)



            

       


