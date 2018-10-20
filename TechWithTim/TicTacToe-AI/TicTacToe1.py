# Tic Tac Toe game in python
# https://www.youtube.com/watch?v=5s_lGC2sxwQ&list=PLzMcBGfZo4-mb4e1J1eKcdI3PquhPt2C7

board = [' ' for x in range[10]]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('  |  |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |  |')
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |  |')
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def isWinner(board, le):
    return (board[7] == le and board[8] == le and board[9] == le) or (
                board[4] == le and board[5] == le and board[6] == le) or (
                       board[1] == le and board[2] == le and board[3] == le) or (
                       board[1] == le and board[4] == le and board[7] == le) or (
                       board[2] == le and board[5] == le and board[8] == le) or (
                       board[3] == le and board[6] == le and board[9] == le) or (
                       board[1] == le and board[5] == le and board[9] == le) or (
                       board[3] == le and board[5] == le and board[7] == le)


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:  # exception if int not entered
            print('Please enter a number!')


def compMove():
    pass


def selectRandom(board):
    pass


def isBoardFull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard()

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            compMove()
            printBoard()
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


main()
