import space, random
class Board:
    """
    Defines the gameboard and numerous functions to define the value of each space
    on the board.

    The board class is essentially a list of rows, each of which contains a set number of spaces.
    """
    is_lost = False
    is_won = False
    def __init__(self, xdim = 5, ydim = 5, num_bomb = 2):
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
        :param gameboard: An empty list that will serve as a container for the spaces. 
            (default is empty)
        :type gameboard: list
        """
        self.xdim, self.ydim = xdim, ydim
        self.num_bomb = num_bomb
        self.gameboard = list()
    
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
            self.gameboard[location[1] * self.xdim + location[0]] = space.Space(is_bomb = True, value = 9)

    def calculate_values(self):
        """
        Calculates the values of every space on the board based on the bomb locations.

        :return: void
        """
        for location in bomb_locations:
            for y in range(-1,2):
                if (location[1] + y != -1) and (location[1] + y != self.ydim):
                    for x in range(-1,2):
                        if (location[0] + x != -1) and (location[0] + x != self.xdim):
                            self.gameboard[((location[1] + y) * self.xdim) + (location[0] + x)].value += 1
    
    def mark_space(self, x_loc:int, y_loc:int):
        """
        Marks a space at the loction specified in the arguments

        :param x_loc: The x location of the space
        :type x_loc: int
        :param y_loc: The y location of the space
        :type y_loc: int
        :return: void
        """
        self.gameboard[y_loc * self.xdim + x_loc].mark_space()

    @staticmethod
    def create_board(gameboard:list, xdim:int, ydim:int):
        """
        Creates an empty two dimensional list of Spaces with the given dimensions.

        :param board: An empty list which will contain the spaces in the game
        :type board: list
        :param xdim: The x dimension of the board
        :type xdim: int
        :param ydim: The y dimension of the board
        :type ydim: int
        """
        for location in range(ydim * xdim):
            gameboard.append(space.Space())

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
        while len(bomb_loc) < num_bomb:
            xloc = random.randint(0, xdim - 1)
            yloc = random.randint(0, ydim - 1)
            new_loc = (xloc, yloc)
            to_add = True
            for location in bomb_loc:
                if location == new_loc:
                    to_add = False

            if to_add:
                bomb_loc.append((xloc, yloc))
        global bomb_locations
        bomb_locations = bomb_loc