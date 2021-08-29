"""
module containing Board class

and some useful functions
"""
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
                      
        return self[position]== None
            
    
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
  

    def show(self):
        """
        prints board in text mode
        """
        # refactor using self._files and self._ranks
        
        files , ranks = self._files, self._ranks 
        print()
        print(f'Board {self._size}x{self._size}')
        print('  +','-'*(len(files)*2+1),'+', sep='' )  #topline

        for rank in reversed(ranks):
            print (rank,'| ', end = '')
            for file in files:
               
                if self._board[rank][file] == None:
                    print ('  ',end = '')
                else:
                    print (self._board[rank][file],' ', sep='',end = '')

            print('|') #right line
        
        print('  +','-'*(len(files)*2+1),'+', sep='' )  #bottomline
        print('   ', end='')
        for file in files:
            print (' ',file,sep='', end='')
        print()

    def create_position(self,from_position,move_vector=(0,0)):
        """
        returns to position from initial position and move vector
        used in determining legal positions
        to position must be on board
        """
        from_file, from_rank = self._parse_position(from_position)
        to_rank = from_rank +move_vector[0]
        if 0 > to_rank or to_rank > self._size:
            return None

        files, _ = self._board_plan()
        file_ord = move_vector[1] + files.find(from_file)
        
        if 0 > file_ord or file_ord > self._size-1:
            return None
        to_file = files[file_ord]
        to_position = to_file+str(to_rank) 

        return to_position if self.is_on_board(to_position) else None

    def move(self, from_position, to_position):

        from_file, from_rank = self._parse_position(from_position)
        to_file, to_rank = self._parse_position(to_position)
        
        

        v_sideways = self._files.find(to_file)-self._files.find(from_file)
        v_ahead = to_rank - from_rank

        if self._board[from_rank][from_file] == None:
            raise ValueError(f'there is nothing on {from_position} position on the board')
            return False
        
        _item = self._board[from_rank][from_file]

              
        move_vector = (v_ahead, v_sideways)

        if move_vector == (0,0):
            print ('move somewhere')
            return False

         
        if _item.within_reach(*move_vector) == 'move' and self.is_free(to_position):

            self._board[from_position]=None
            self._board[to_position]=_item
            print (f'move vector is :{v_ahead}, {v_sideways}, type PUSH')
            return 'push' # is within reach and position to is free
    
        elif _item.within_reach(*move_vector) == 'take' and (
            not self.is_free(to_position) and not _item.same_color(self.get_item(to_position))
            ):

            self.board[from_position]=None
            self.board[to_position]=_item
            print (f'move vector is :{v_ahead}, {v_sideways}, type TAKE')
            return 'take' # if within take reach and position to is occupied by opposing color piece
    
        else:
            print (f'move vector is :{v_ahead}, {v_sideways}, type FALSE')
            return False


    def has_legal_moves(self, *positions):
        legal_moves = []
        for position in positions: # through all positions
            
            piece = self.get_item(position)
            for move in piece.legal_moves()['move']:
                
                to_position = self.create_position(position,move)
                if to_position == None:
                    
                    continue
                
                if self.is_free(to_position):

                    
                    legal_moves.append(to_position)
                else:
                    pass

                
            for take in piece.legal_moves()['take']:
                
                to_position = self.create_position(position,take)

                if to_position == None:
                    
                    continue
                if self.is_free(to_position) or piece.same_color(self.get_item(to_position)):
                    continue
                else:
                    legal_moves.append(to_position)
                    
                
        return legal_moves     
        
    

      
        
    
    
        