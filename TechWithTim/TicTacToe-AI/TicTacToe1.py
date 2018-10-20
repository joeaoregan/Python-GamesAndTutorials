# Tic Tac Toe game in python
# https://www.youtube.com/watch?v=5s_lGC2sxwQ&list=PLzMcBGfZo4-mb4e1J1eKcdI3PquhPt2C7

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, le):
    return (board[7] == le and board[8] == le and board[9] == le) or (  # across top row
            board[4] == le and board[5] == le and board[6] == le) or (  # across middle row
                   board[1] == le and board[2] == le and board[3] == le) or (  # across bottom row
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
    possibleMoves = [x for x, letter in enumerate(board) if
                     letter == ' ' and x != 0]  # always a blank indices at beginning of list
    move = 0  # default move is to place in the middle of the board

    # check if computer can win, or if player can win block
    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]  # clone/make a copy in memory
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)  # create a random number between 0 and length of list
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


if __name__ == "__main__":
    main()

