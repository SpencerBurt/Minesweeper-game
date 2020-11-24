'''import functions
from tkinter import *

root = Tk()
'''
import functions as func, board
def main():
    xdim = int(input("Enter the x dimension: \n"))
    ydim = int(input("Enter the y dimension: \n"))
    num_bomb = int(input("Enter the number of bombs: \n"))
    gameboard = board.Board(xdim, ydim, num_bomb)
    gameboard.make_board()
    func.Functions.print_board(gameboard)
    first_x = input("Enter x location: \n")
    first_y = input("Enter y location: \n")
    func.Functions.reveal_space(gameboard, int(first_x), int(first_y))
    is_won = False

    while not is_won:
        func.Functions.print_board(gameboard)
        move = input("[R] Reveal    [M] Mark    [Q] Quit\n")
        if move.capitalize() == "R":
            xloc = int(input("Enter x location: \n"))
            yloc = int(input("Enter y location: \n"))
            if xloc >= xdim or yloc >= ydim:
                print("Incorrect input, space is out of bounds")
                continue
            func.Functions.reveal_space(gameboard, xloc, yloc)
        elif move.capitalize() == "Q":
            break
        elif move.capitalize() == "M":
            xloc = int(input("Enter x location: \n"))
            yloc = int(input("Enter y location: \n"))
            gameboard.mark_space(xloc, yloc)
        else:
            print("Please enter a valid move")
            continue
        if gameboard.is_lost:
            restart = input("You hit a bomb! Restart?\n[Y] Yes    [N] No\n")
            if restart.capitalize() == "Y":
                main()
            else:
                break
    print("Thanks for playing!")

    


if __name__ == "__main__":
    main()