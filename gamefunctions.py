import random

class Functions:
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
        bomb_locations = Board.generate_bomb_loc(self.num_bomb, self.xdim, self.ydim)
        for location in bomb_locations:
            self.gameboard[location[0]][location[1]] = Space(is_bomb = True)

    def calculate_values(self):
        x = 0
        y = 0
        for row in self.gameboard:
            for space in row:
                for temp_y in range(y-1, y+1):
                    #value = 0
                    for temp_x in range(x-1, x+1):
                        if (temp_x != -1) and (temp_y != -1) and (temp_x < self.xdim) and (temp_y < self.ydim):
                            if self.gameboard[temp_y][temp_x].is_bomb:
                                #value += 1
                                space.value += 1
                x +=1
            y +=1

    @staticmethod
    def create_board(board, xdim, ydim):
        for y in range(ydim):
            board.append([Space()])
            for x in range(xdim-1):
                board[y].append(Space())

    @staticmethod
    def generate_bomb_loc(num_bomb, xdim, ydim):
        bomb_locations = list()
        for i in range(num_bomb):
            xloc = random.randint(0, xdim-1)
            yloc = random.randint(0, ydim-1)
            bomb_locations.append((xloc, yloc))
        return bomb_locations

def main():
    game_board = Board()
    Functions.print_board(game_board)


if __name__ == "__main__":
    main()
