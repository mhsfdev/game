"""
module containing Board class

and some useful functions
"""
class Board :
    
    def __init__(self,size = None):
        """
        board is defined as list of dictionaries where
        list index represents rank 1,2 - size
        dictionary keys represent file designations A, B... size up to H
        """
        if size>8:
            raise ValueError('Board max is 8')
        self.size = size

        files, ranks = self._board_plan() 
        self.board = [None] + [{letter : None for letter in files}  for _ in ranks] 

    def _board_plan(self): #creates file and rank designations as iterables
        return ("ABCDEFGH"[:self.size],range(1,self.size+1))

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
        boolean, checks if position is on the board
        args:
          string / position in filerank notation
        """
        files, ranks = self._board_plan()
        rank_text = position[1]
        file = position.upper()[0] # parse file designator , make it upper in case lower case is used
        if len(position)!=2:
            return False
        
        try:
            rank = int(rank_text)
        except ValueError :
            return False
        
        if rank not in ranks:
            return False
             
        if file not in files :
            return False
        
        return True
    
    def is_free(self, position):
        """ boolean
        returns True if position on Board is not None = taken by object
        arg - posiiton in filerank notation
        """
        
        file, rank = self._parse_position(position)
        
        if self.board[rank][file] != None:
            return False
        else :
            return True
    
    def get_item(self, position):
        """
        returns whatever is on the position (arg)on the board
        if there is nothing, method returns None
        """
        file, rank = self._parse_position(position)
        if not self.is_free(position):
            return self.board[rank][file]
        else:
            return None

       

    def place_item(self, piece, position):
        """ 
        Positions piece on the designated position
        args :
            piece = item to be placed
            position = file, rank notation 'A1'
        """
        file, rank = self._parse_position(position)
        if self.is_free(position):
            self.board[rank][file] = piece # in datastructure is the board transposed 
        else:
            raise ValueError(f'Position {position} is not free')

    def show(self):
        """
        prints board in text mode
        """
        files , ranks = self._board_plan()
        print()
        print(f'Board {self.size}x{self.size}')
        print('  +','-'*(len(files)*2+1),'+', sep='' )  #topline

        for rank in reversed(ranks):
            print (rank,'| ', end = '')
            for file in files:
               
                if self.board[rank][file] == None:
                    print ('  ',end = '')
                else:
                    print (self.board[rank][file],' ', sep='',end = '')

            print('|') #right line
        
        print('  +','-'*(len(files)*2+1),'+', sep='' )  #bottomline
        print('   ', end='')
        for file in files:
            print (' ',file,sep='', end='')
        print()

    def move(self, from_position, to_position):

        """ 
        method processing the movement of the Piece on the boar.

        checks movement abilities of the Piece on the from position
        checks to position to be on the board, within reach of the Piece
        type of the movement - push or take
        """
        
        from_file, from_rank = self._parse_position(from_position)
        to_file, to_rank = self._parse_position(to_position)
        #compute vector as Tuple(number of field in forward direction, sideways direction)
        files, _ = self._board_plan()
        v_sideways = files.find(to_file)-files.find(from_file)
        v_ahead = to_rank - from_rank
        vector =(v_ahead,v_sideways)

        if self.board[from_rank][from_file] == None:
            raise ValueError(f'there is nothing on {from_position} position on the board')
        
        _item = self.board[from_rank][from_file]

      
        self.board[from_rank][from_file]=None
        self.board[to_rank][to_file]=_item
        