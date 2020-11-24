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
        for row in board.gameboard:
            for space in row:
                print(space, end=" ")
            print()

    @staticmethod
    def reveal_space(board:board.Board, xloc:int, yloc:int):
        space = board.gameboard[yloc][xloc]
        coordinates = (yloc, xloc)
        if space.is_marked:
            Functions.reveal_marked()
        elif space.is_bomb:
            board.is_lost = True
            #Functions.lose()
        elif not space.is_hidden:
            Functions.reveal_revealed()
        else:
            space.is_hidden = False
            for y in range(-1,2):
                if (coordinates[0] + y != -1) and (coordinates[0] + y != board.ydim):
                    for x in range(-1,2):
                        if (coordinates[1] + x != -1) and (coordinates[1] + x != board.xdim):
                            if board.gameboard[coordinates[0]+y][coordinates[1]+x].value == 0:
                                board.gameboard[coordinates[0]+y][coordinates[1]+x].is_hidden = False

    @staticmethod
    def lose():
        print("You lose!")

    @staticmethod
    def reveal_marked():
        print("Space is marked, unmark it to reveal.")

    @staticmethod
    def reveal_revealed():
        print("Space is already revealed.")