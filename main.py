class Board :
    
    def __init__(self,size = None):
        self.size = size
        files, ranks = self._board_plan() 
        self.board = [None] + [{letter : None for letter in files}  for _ in ranks]

    def _board_plan(self): #creates file and rank designations as iterables
        return ("ABCDEFGH"[:self.size],range(1,self.size+1))

    def _parse_position(self, position):
        files, ranks = self._board_plan()
        rank_text = position[-1]

        try:
            rank = int(rank_text)
        except ValueError :
            raise ValueError (f' rank {rank} not number ')
        if rank not in ranks:
            raise ValueError (f'rank {rank} outside the board')
        
        file = position[0]

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
        pass


    


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
        
        
    

size = 3
b=Board(size)

for line in reversed(range(1,size+1)):
    print(f'{line}: {b.board[line]}')


b.place_item( Piece('b'), 'A1')
b.place_item( Piece('b'), 'B1')

b.visualize()

            

       


