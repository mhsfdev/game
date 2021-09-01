"""
module containing Board class

and some useful functions
"""
from pieces import Piece
import copy

class Board :
    MAX_SIZE = 8
    
    def __init__(self,size = None):
        """
        board is defined as list of dictionaries where
        list index represents rank 1,2 - size
        dictionary keys represent file designations A, B... size up to H
        """
        if size>8:
            raise ValueError('Board max is 8')
        self._size = size

        self._files, self._ranks = self._board_plan() 
        self._board = [None] + [{letter : None for letter in self._files}  for _ in self._ranks] 

    @property
    def size(self):
        return self._size
    
    def _board_plan(self): #creates file and rank designations as iterables
        return ("ABCDEFGH"[:self._size],range(1,self._size+1))

    def _parse_position(self, position): # filerank notation A1
        """
        checks if position is on the board and returns tuple (File, rank)
        args = position in filerank notation
        """
        
        if self.is_on_board(position): 
            return  position.upper()[0],int(position[-1])
        else:
            raise ValueError(f'Position {position} not valid')
    
    def is_on_board(self, position):
        """
        core method checking validity of position and if it is on board
        boolean
        args:
          string / position in filerank notation
        """
        
        rank_text = position[1]
        file = position.upper()[0] # parse file designator , make it upper in case lower case is used
        if len(position)!=2:
            return False
        
        try:
            rank = int(rank_text)
        except ValueError :
            return False
        
        if rank not in self._ranks or file not in self._files:
            return False
             
        return True
    
    
    def is_free(self, position):
        """ boolean
        returns True if position on Board is not None = taken by object
        arg - posiiton in filerank notation
        """
                      
        return self[position] == None
            
    
    def __getitem__(self, position):
        """
        returns whatever is on the position (arg)on the board
        if there is nothing, method returns None
        """
        file, rank = self._parse_position(position)
        
        return self._board[rank][file]
       

    def __setitem__(self, position, piece):
        """ 
        Positions piece on the designated position
        args :
            piece = item to be placed
            position = file, rank notation 'A1'
        """
        file, rank = self._parse_position(position)
        self._board[rank][file] = piece # in datastructure is the board transposed 
    
    def setup_pieces(self, positions = [], piece = None): #not tested!!!
  
        """
        sets piece on designated positions on all or nothing principle
        """
	 
        if not isinstance(piece, Piece):
            raise ValueError (f'item {piece} is not valid piece')
          
        
        for position in positions:
            if not self.is_on_board(position) :
                raise ValueError(f'position{position} is not valid, none of {positions} will be set up')

        for position in positions:
            self[position] = piece


    def show(self):
        """
        prints board in text mode
        """
        # refactor using self._files and self._ranks
        
        
        print()
        print(f'Board {self._size}x{self._size}')
        print('  +','-'*(self._size*2+1),'+', sep='' )  #topline

        for rank in reversed(self._ranks):
            print (rank,'| ', end = '')
            for file in self._files:
               
                if self._board[rank][file] == None:
                    print ('  ',end = '')
                else:
                    print (self._board[rank][file],' ', sep='',end = '')

            print('|') #right line
        
        print('  +','-'*(self._size*2+1),'+', sep='' )  #bottomline
        print('   ', end='')
        for file in self._files:
            print (' ',file,sep='', end='')
        print()

    def calculate_position(self,from_position,move_vector=(0,0)):
        """
        returns to position from initial position and move vector
        used in determining legal positions
        to position must be on board
        move vector(filesmovement, rankmovement)
        """
        from_file, from_rank = self._parse_position(from_position)
        to_rank = from_rank +move_vector[0]
        if 0 > to_rank or to_rank > self._size:
            raise ValueError

        files, _ = self._board_plan()
        file_ord = move_vector[1] + files.find(from_file)
        
        if 0 > file_ord or file_ord > self._size-1:
            return None
        to_file = files[file_ord]
        to_position = to_file+str(to_rank) 

        if self.is_on_board(to_position):
            return to_position
        else:
            raise ValueError('new position {to_position} is out of the board')

    def _move_vector(self, position1, position2):
        
        if (self.is_on_board(position1) and self.is_on_board(position2)) != True:
            raise ValueError
        
        from_file, from_rank = self._parse_position(position1)
        to_file, to_rank = self._parse_position(position2)
        
        v_sideways = self._files.find(to_file)-self._files.find(from_file)
        v_ahead = to_rank - from_rank
        
        return (v_ahead, v_sideways)

    def move(self, from_position, to_position):
        move_vector = self._move_vector(from_position, to_position)

        if self[from_position] == None:
            raise ValueError(f'there is nothing on {from_position} position on the board')
            
        _item = self[from_position]
        
        if move_vector == (0,0):
            print ('move somewhere')
            return False

         
        if _item.within_reach(move_vector) == 'move' and self.is_free(to_position):

            self[from_position] = None
            self[to_position] = _item
            
            return 'push' # is within reach and position to is free
    
        elif _item.within_reach(move_vector) == 'take' and (
            not self.is_free(to_position) and not _item.same_color(self[to_position])
            ):

            self[from_position]=None
            self[to_position]=_item
            
            return 'take' # if within take reach and position to is occupied by opposing color piece
    
        else:
            
            return False


    def has_legal_moves(self, *positions):
        '''
        generates set of positions reachable by legal move from positions sent as argument
        '''
        legal_positions_to_move = []
        for position in positions: # through all positions
            
            piece = self[position]
            for move in piece.legal_moves()['move']:
                
                to_position = self.calculate_position(position,move)
                if to_position == None:
                    
                    continue
                
                if self.is_free(to_position) and (to_position not in legal_positions_to_move):
                    legal_positions_to_move.append(to_position)
                else:
                    pass

                
            for take in piece.legal_moves()['take']:
                
                to_position = self.calculate_position(position,take)

                if to_position == None: #??? dont get it??
                    
                    continue
                if self.is_free(to_position) or piece.same_color(self[to_position]):
                    continue
                elif (to_position not in legal_positions_to_move):
                    legal_positions_to_move.append(to_position)
                else:
                    continue
                    
                
        return legal_positions_to_move
        
class PawnGameBoard(Board):

    """
    derived class from Board class specifying starting positions, winning positions on board and allowed pieces
    """
    def __init__(self, size = 3):
        super().__init__(size)
        self._starting_positions_black = [
            char + str(self.size) for char in self._files # top row depending on size
        ]
        self._starting_positions_white = [
            char + '1' for char in self._files # bottom row
        ]
    
        

    @property
    def starting_positions_black(self):
        """
        returns list of starting position for the black player
        """    
        return self._starting_positions_black
   
    @property
    def starting_positions_white(self):
        """
        returns list of starting position for the white player
        """    
        return self._starting_positions_white
   
    
    def winning_positions(self, color=None):
        if color in ['black','b', 'B']:
            return self._starting_positions_white
   
        elif color in ['white','w', 'W']:
            return self._starting_positions_black
        else :
            return None


      
        
    
    
        