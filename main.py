from board import Board
from pieces import Pawn
from player import Player


 

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
             
                
        if not players[playing_player].his_position(from_position):
            print (f'You do not have piece on position {from_position}')
            continue

        if b.is_valid(from_position, to_position):
             
            if to_position in players[opposing_player].pieces.keys() :
                del players[opposing_player].pieces[to_position] # deletion from the players set

            del players[playing_player].pieces[from_position]
            players[playing_player].pieces[to_position] = b.get_item(from_position)

            b.move(from_position, to_position)

            b.show()
            turn += 1
            print(player_A.name, player_A.pieces)
            print(player_B.name, player_B.pieces)
        else :
            print('not valid move , buddy')


if __name__ == '__main__':
    main()
        



            

       


