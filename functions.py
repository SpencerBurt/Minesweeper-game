import board
class Functions:
    """
    Provides some of the utility functions for printing and interacting with the gameboard.
    """
    @staticmethod
    def print_board(board:board.Board):
        """
        Prints the gameboard
    
        :param board: The gameboard that will be printed
        :type board: Board
        :returns: void
        """
        for y in range(board.ydim):
            for x in range(board.xdim):
                print(board.gameboard[y * board.xdim + x], end= '')
            print()
            

    @staticmethod
    def reveal_space(board:board.Board, xloc:int, yloc:int):
        """
        Decides whether or not to reveal a space on the board given the user's input

        :param board: The board
        :type board: Board
        :param xloc: The x location to be checked
        :type xloc: int
        :param yloc: The y location to be checked
        :type yloc: int
        :returns: void
        """
        space = board.gameboard[yloc * board.xdim + xloc]
        if space.is_marked:
            Functions.reveal_marked()
        elif space.is_bomb:
            board.is_lost = True
        elif not space.is_hidden:
            Functions.reveal_revealed()
        else:
            Functions.reveal_zeros(board, xloc, yloc, space)
            
    # Note: the function declaration sacrifices some simplicity to avoid having to import the space file, this could be simplified later on if problems arise.
    @staticmethod
    def reveal_zeros(board:board.Board, xloc:int, yloc:int, space:board.space.Space):
        """
        Reveals a given space. Reveals the surrounding spaces if it is zero.

        :param board: The board
        :type board: Board
        :param xloc: The x location of the space being revealed
        :type xloc: int
        :param yloc: The y location of the space being revealed
        :type yloc: int
        :param space: The space being revealed, determined by the reveal_space function
        :type space: Space
        :returns: void
        """
        space.is_hidden = False
        if space.value == 0:
            for y in range(-1,2):
                if (yloc + y != -1) and (yloc + y != board.ydim):
                    for x in range(-1,2):
                        location = board.gameboard[(yloc + y) * board.xdim + (xloc + x)]
                        if (xloc + x != -1) and (xloc + x != board.xdim) and not location.is_bomb:
                            location.is_hidden = False

    @staticmethod
    def check_won(board:board.Board):
        is_won = True
        for yloc in range(board.ydim):
            for xloc in range(board.xdim):
                location = board.gameboard[yloc * board.xdim + xloc]
                if location.is_hidden and not location.is_bomb:
                    is_won = False
        board.is_won = is_won

    @staticmethod
    def reveal_marked():
        print('Space is marked, unmark it to reveal.')

    @staticmethod
    def reveal_revealed():
        print('Space is already revealed.')