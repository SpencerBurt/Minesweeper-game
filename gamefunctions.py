import random

class Functions:
    """
    Provides some of the utility functions for printing and interacting
    with the gameboard.

    At the moment, this class only contains the print_board function
    and should not be instantiated.
    """
    @staticmethod
    def print_board(board):
        """
        Prints the gameboard

        :param board: The gameboard that will be printed
        :type board: Board
        :returns: void
        """
        for row in board.gameboard:
            for space in row:
                print(space, end="")
            print()


class Space:
    """
    Stores the value of a space as well as whether or not it is
    marked, hidden, or a bomb.
    """
    def __init__(self, value = 0, is_marked = False, is_bomb = False, is_hidden = True):
        """
        Constructor for the Space class.

        :param value: The value of the space
        :type value: int
        :param is_marked: Whether or not the space is marked
        :type is_marked: bool
        :param is_bomb: Whether or not the space is a bomb
        :type is_bomb: bool
        :param is_hidden: Whether or not the space is hidden
        :type is_hidden: bool
        """
        self.value = value
        self.is_marked = is_marked
        self.is_bomb = is_bomb
        self.is_hidden = is_hidden

    @classmethod
    def mark_space(self):
        """
        Marks a space.

        If the space is already marked, this function will unmark it.
        :return: void
        """
        if self.is_marked:
            self.is_marked = False
        else:
            self.is_marked = True

    def __str__(self):
        if self.is_marked:
            return "M"
        elif self.is_hidden:
            return "*"
        else:
            return str(self.value)


class Board:
    """
    Defines the gameboard and numerous functions to define the value of each space
    on the board.

    The board class is essentially a list of rows, each of which contains a set number of spaces.
    """
    def __init__(self, xdim = 5, ydim = 5, num_bomb = 2, gameboard = list()):
        """
        Constructor for the Board class. Creates a variable gameboard that is used as the board
        throughout the class.

        :param xdim: Gives the x dimension of the board.
            (default is 5)
        :type xdim: int
        :param ydim: Gives the y dimension of the board.
            (default is 5)
        :type ydim: int
        :param num_bomb: Gives the number of bombs on the board.
            (default is 2)
        :type num_bomb: int
        """
        self.xdim = xdim
        self.ydim = ydim
        self.num_bomb = num_bomb
        self.gameboard = gameboard
    
    def make_board(self):
        """
        Calls the create_board, create_bombs, and calculate_values functions to create a full board.

        :return: void
        """
        Board.create_board(self.gameboard, self.xdim, self.ydim)
        self.create_bombs()
        self.calculate_values()

    def create_bombs(self):
        """
        Calls the generate_bomb_loc function to generate a list of bomb locations that 
        are then used to change the spaces at those locations to bombs.

        :return: void
        """
        Board.generate_bomb_loc(self.num_bomb, self.xdim, self.ydim)
        print(bomb_locations)
        for location in bomb_locations:
            self.gameboard[location[0]][location[1]] = Space(is_bomb = True)

    def calculate_values(self):
        """
        Calculates the values of every space on the board based on the bomb locations.

        :return: void
        """
        for location in bomb_locations:
            for y in range(-1,2):
                if (location[0] + y != -1) and (location[0] + y != self.ydim):
                    for x in range(-1,2):
                        if (location[1] + x != -1) and (location[1] + x != self.xdim):
                            self.gameboard[location[0]+y][location[1]+x].value +=1        

    @staticmethod
    def create_board(board:list, xdim:int, ydim:int):
        """
        Creates an empty two dimensional list of Spaces with the given dimensions.

        :param board: An empty list which will contain the spaces in the game
        :type board: list
        :param xdim: The x dimension of the board
        :type xdim: int
        :param ydim: The y dimension of the board
        :type ydim: int
        """
        for y in range(ydim):
            board.append([Space()])
            for x in range(xdim-1):
                board[y].append(Space())

    @staticmethod
    def generate_bomb_loc(num_bomb, xdim, ydim):
        """
        Generates a list of tuples that store the randomized locations of the bombs.

        :param num_bomb: The number of bombs in the game
        :type num_bomb: int
        :param xdim: The x dimension of the board
        :type xdim: int
        :param ydim: The y dimension of the board
        :type ydim: int
        """
        bomb_loc = list()
        for i in range(num_bomb):
            xloc = random.randint(0, xdim-1)
            yloc = random.randint(0, ydim-1)
            bomb_loc.append((yloc, xloc))
        global bomb_locations
        bomb_locations = bomb_loc
    

def main():
    game_board = Board(xdim=10, ydim=10, num_bomb=3)
    game_board.make_board()
    Functions.print_board(game_board)


if __name__ == "__main__":
    main()
