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
        for row in board.gameboard:
            for space in row:
                if space.is_bomb:
                    print('b',end='')
                elif space.is_marked:
                    print('M', end='')
                else:
                    print(str(space.value), end='')
            print()


class Space:
    is_marked = False
    def __init__(self, value = 0, is_marked = False, is_bomb = False, is_hidden = True):
        self.value = value
        self.is_marked = is_marked
        self.is_bomb = is_bomb
        self.is_hidden = is_hidden

    @classmethod
    def mark_space(self):
        if self.is_marked:
            self.is_marked = False
        else:
            self.is_marked = True


class Board:
    xdim = 0
    ydim = 0
    num_bomb = 0
    gameboard = list()

    def __init__(self, xdim = 5, ydim = 5, num_bomb = 2, gameboard = list()):
        self.xdim = xdim
        self.ydim = ydim
        self.num_bomb = num_bomb
        self.gameboard = gameboard
        Board.create_board(self.gameboard, self.xdim, self.ydim)
        self.create_bombs()
        self.calculate_values()

    def create_bombs(self):
        Board.generate_bomb_loc(self.num_bomb, self.xdim, self.ydim)
        print(bomb_locations)
        for location in bomb_locations:
            self.gameboard[location[0]][location[1]] = Space(is_bomb = True)

    def calculate_values(self):
        for location in bomb_locations:
            for y in range(-1,2):
                if (location[0] + y != -1) and (location[0] + y != self.ydim):
                    for x in range(-1,2):
                        if (location[1] + x != -1) and (location[1] + x != self.xdim):
                            self.gameboard[location[0]+y][location[1]+x].value +=1
                    

    @staticmethod
    def create_board(board, xdim, ydim):
        for y in range(ydim):
            board.append([Space()])
            for x in range(xdim-1):
                board[y].append(Space())

    @staticmethod
    def generate_bomb_loc(num_bomb, xdim, ydim):
        bomb_loc = list()
        for i in range(num_bomb):
            xloc = random.randint(0, xdim-1)
            yloc = random.randint(0, ydim-1)
            bomb_loc.append((yloc, xloc))
        global bomb_locations
        bomb_locations = bomb_loc

def main():
    game_board = Board(xdim=10, ydim=10, num_bomb=3)
    Functions.print_board(game_board)


if __name__ == "__main__":
    main()
