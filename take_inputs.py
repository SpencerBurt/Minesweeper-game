from functions import Functions
from board import Board
def main():
    xdim = int(input('Enter the x dimension: \n'))
    ydim = int(input('Enter the y dimension: \n'))
    num_bomb = int(input('Enter the number of bombs: \n'))
    gameboard = Board(xdim, ydim, num_bomb)
    gameboard.make_board()
    Functions.print_board(gameboard)
    first_x, first_y = xdim + 1, ydim + 1
    
    while first_x > (xdim - 1):
        first_x = int(input('Enter x location: \n'))
        if first_x > (xdim - 1):
            print('Please enter a value less than ' + xdim)
    while first_y > (ydim - 1):
        first_y = int(input('Enter y location\n'))
        if first_y > (ydim - 1):
            print('Please enter a value less than ' + ydim)

    if not Functions.reveal_space(gameboard, int(first_x), int(first_y)):
        print('Tough luck! You hit a bomb, restarting...', end='')
        main()

    while Functions.move(gameboard):
        if Functions.check_won(gameboard):
            print('You Won! ', end='')
            restart = input('You hit a bomb! Restart?\n[Y] Yes    [N] No\n')
            if restart.capitalize() == 'Y':
                main()
                break
            else:
                break
        if gameboard.is_lost:
            restart = input('You hit a bomb! Restart?\n[Y] Yes    [N] No\n')
            if restart.capitalize() == 'Y':
                main()
            else:
                break

    print('Thanks for playing!')

if __name__ == "__main__":
    main()