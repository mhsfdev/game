from board import Board
from pieces import Pawn
from player import Player



size = 5
b = Board(size)
p_b = Pawn('b')
p_w = Pawn('w')

player_A = Player('Hugo', 'b')
player_B = Player('Elvis', 'w')

player_A.set_piece(['a3', 'b3', 'c3'], p_b)

player_B.set_piece(['a2', 'b2', 'c2'], p_w)
players = [player_A, player_B]

for position, piece in player_A.pieces.items():
    b.place_item(piece, position)

for position, piece in player_B.pieces.items():
    b.place_item(piece, position)

turn = 1
b.show()

opposing_player = 0

while len(b.has_legal_moves(*players[opposing_player].pieces.keys())) != 0: #winning condition, opposing player has no valid moves
    playing_player = turn % 2
    opposing_player = (playing_player + 1) % 2

    

    try:  # taking move to do
        from_position, to_position = input(
            f'whats your next move {players[playing_player]}? ').split(',')
        from_position, to_position = from_position.strip(
        ), to_position.strip()  # stripped of unneccessary blanks
    except ValueError:
        break

    if not players[playing_player].his_position(from_position):
        print(f'You do not have piece on position {from_position}')
        continue

    moving_piece = b.get_item(from_position)

    move = b.move(from_position, to_position)

    if move in ('take', 'push'):  # in case of valid move

        if move == 'take':  # take the oponents piece away
            del players[opposing_player].pieces[
                to_position]  # deletion from the players set

        del players[playing_player].pieces[
            from_position]  # delete record on from position
        players[playing_player].pieces[
            to_position] = moving_piece  # create record on to position

        b.show()
        turn += 1
        
    else:

        print('not valid move , buddy')

print (f'game over for player {players[playing_player]} he has not valid moves to make !!!' )

