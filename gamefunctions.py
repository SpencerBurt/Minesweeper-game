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
        bomb_loc = Board.generate_bomb_loc(self.num_bomb, self.xdim, self.ydim)
        global bomb_locations
        bomb_locations = bomb_loc
        print(bomb_locations)
        for location in bomb_locations:
            self.gameboard[location[0]][location[1]] = Space(is_bomb = True)

    def calculate_values(self):
        '''
        for x in range(0, self.xdim):
            for y in range(0, self.ydim):
                for temp_y in range(y-1, y+1):
                    if (temp_y >= 0) and (temp_y < self.ydim):
                        for temp_x in range(x-1, x+1):
                            if (temp_x >= 0) and (temp_x < self.xdim):
                                if self.gameboard[temp_y][temp_x].is_bomb:
                                    self.gameboard[y][x].value += 1'''
        for location in bomb_locations:
            '''
            self.gameboard[location[0]+1][location[1]]      #same column, one row below
            self.gameboard[location[0]-1][location[1]]      #same column, one row above
            self.gameboard[location]'''
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
        bomb_locations = list()
        for i in range(num_bomb):
            xloc = random.randint(0, xdim-1)
            yloc = random.randint(0, ydim-1)
            bomb_locations.append((yloc, xloc))
        return bomb_locations

def main():
    game_board = Board()
    Functions.print_board(game_board)


if __name__ == "__main__":
    main()
