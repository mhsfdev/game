from board import PawnGameBoard
from pieces import Pawn, Piece
from player import Player


def standardise_position(position):
    if len(position) !=2:
            position = position[:2]
        
    file = position.upper()[0]
    rank = str(position[1])
        
    return file+rank

def main():
    
    
    #game setup
    
    b = PawnGameBoard() # 3 is base value
    black_pawn = Pawn('b')
    white_pawn = Pawn('w')

    #player setup

    player_black = Player('Hugo', color = black_pawn.color)
    player_white = Player('Elvis', color = white_pawn.color)

    #setting up pieces for players    
    player_black.set_piece(b.starting_positions_black, black_pawn)
    print(player_black,'\n', player_black.pieces)
    player_white.set_piece(b.starting_positions_white, white_pawn)
    print(player_white,'\n',player_white.pieces)
    players = [player_black, player_white]
    
    
    #setting up pieces on the  board
    b.setup_pieces(b.starting_positions_black, black_pawn)
    b.setup_pieces(b.starting_positions_white, white_pawn)
    

    turn = 1
    b.show()



    while len(b.has_legal_moves(*players[turn%2].pieces.keys())) != 0: #winning condition, opposing player has no valid moves
        playing_player = turn % 2
        opposing_player = (playing_player + 1) % 2

        
        if players[playing_player].is_human:
            try:  # taking move to do
                from_position, to_position = input(
                    f'whats your next move {players[playing_player]}? ').split(',')
                from_position, to_position = from_position.strip(
                ), to_position.strip()  # stripped of unneccessary blanks
            except ValueError:
                break
        
        else:
            #create function to do legal move by CPU
            pass


        from_position = standardise_position(from_position)
        to_position = standardise_position(to_position)
        


        if not players[playing_player].his_position(from_position):
            print(f'You do not have piece on position {from_position}')
            continue

        moving_piece = b[from_position]
        try:
            move = b.move(from_position, to_position)

            if move in ('take', 'push'):  # in case of valid move

                if move == 'take':  # take the oponents piece away
                    del players[opposing_player].pieces[to_position]  # deletion from the players set

                del players[playing_player].pieces[from_position]  # delete record on from position
                players[playing_player].pieces[to_position] = moving_piece  # create record on to position

                b.show()
                # winning positioncondition on exit
                if to_position in b.winning_positions(color = players[playing_player].color):
                    print (f'game won by player {players[turn%2]} he has reached winning position {to_position} !!!' )
                    break
                turn += 1
                
        except:

            print('not valid move , buddy')
    else: #no break exit
        print (f'game over for player {players[turn%2]} he has not valid moves to make !!!' )


if __name__ =='__main__':
    main()