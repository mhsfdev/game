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
            raise ValueError(f'Board max is 8')
        self.size = size

        files, ranks = self._board_plan() 
        self.board = [None] + [{letter : None for letter in files}  for _ in ranks] 

    def _board_plan(self): #creates file and rank designations as iterables
        return ("ABCDEFGH"[:self.size],range(1,self.size+1))

    def _parse_position(self, position): # filerank notation A1
        files, ranks = self._board_plan()
        rank_text = position[-1]

        try:
            rank = int(rank_text)
        except ValueError :
            raise ValueError (f' rank {rank} not number ')
        if rank not in ranks:
            raise ValueError (f'rank {rank} outside the board')
        
        file = position.upper()[0] # parse file designator , make it upper in case lower case is used

        if file not in files :
            raise ValueError (f'file {file} outside the board')
        
        return  file,rank

    def place_item(self, piece, position):
        """ 
        Positions piece on the designated position
        args :
            piece = item to be placed
            position = file, rank notation 'A1'
        """
        
        file, rank = self._parse_position(position)
        
        if self.board[rank][file] != None:
            raise ValueError (f'Position {position} is already taken')
        
        self.board[rank][file] = piece # in datastructure is the board transposed 

    def visualize(self):
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
        def _within_reach(piece):# inner method deciding if new place is in the reach
            return True
        
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

        if _within_reach(_item):
            self.board[from_rank][from_file]=None
            self.board[to_rank][to_file]=_item
            return(f'move completed with move vector : {vector}')
        else:
            return(f'move out of reach for the piece on {from_position} position')