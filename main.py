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
        self.pieces = []
        if color not in ['b','w']:
            raise ValueError(f'Color {color} is not valid')
    
    def set_pieces(self, piece, positions):
        for position in positions:
            self.pieces.append([piece, position])
    
    def remove_piece(self, position): # find record with position and remove it from the list
        pass





    
        

size = 3
b=Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

player_A = [[p_b,'a1'],[p_b,'b1'],[p_b,'c1']]
player_B = [[p_w,'a3'],[p_w,'b3'],[p_w,'c3']]
players = [player_A,player_B]

for piece, position in player_A:
    b.place_item(piece, position)

for piece, position in player_B:
    b.place_item(piece, position)
turn = 1
b.visualize()
while True:
    playing_player = turn%2
    
    try: # taking move to do
        from_position, to_position =  input(f'whats next move {players[playing_player]}? ').split(',')
    except ValueError:
        break
    
    if b.is_free(to_position): # if destination is free, move i done, turn is completed
        b.move(from_position, to_position)
        turn +=1
    else:
        piece_out = b.get_item(to_position) # if destination is taken by friendly piece
        if b.get_item(from_position).color == piece_out.color:
            print('you fool, there is your piece!! Again')
            continue # turn is not completed 

        b.move(from_position, to_position)

    b.visualize()
    print(player_A)
    print(player_B)



            

       


