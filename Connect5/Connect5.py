# Joe O'Regan
# 11/02/2019
# Connect5.py

from array import *

ROW, COL, PLAYER_1, PLAYER_2 = 6, 9, 1, 2


class Game:
    def __init__(self):
        self.currentPlayer = PLAYER_1
        self.gameOver = False
        self.board = [[0 for col in range(COL)] for row in range(ROW)]   # init board to all 0's

    def getGameOver(self):
        return self.gameOver

    # Draw the board
    def drawBoard(self):
        print("0 1 2 3 4 5 6 7 8")
        for r in self.board:
            for c in r:
                print(c,end = " ")
            print()

    # Check the column is not full, and add player move
    def checkCol(self, column):
        if column >= COL or column < 0:
            print("ERROR: Invalid column number!")
            return False

        if self.board[0][column] != 0:
            print("Error: Column is full")
            return False

        for r in range(ROW - 1, -1, -1):
            if self.board[r][column] == 0:
                self.board[r][column] = self.currentPlayer
                print("Move Added To Board")
                break
        print()
        return True

    def checkWin(self):
        for row in range(0, ROW - 4):
            for col in range(4, COL):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row + 1][col - 1] and self.board[row][col] == self.board[row + 2][col - 2] and self.board[row][col] == self.board[row + 3][col - 3] and self.board[row][col] == self.board[row + 4][col - 4]:
                    self.gameOver = True
                    break

            for col in range(0, COL - 4):
                if self.board[row][col] != 0 and self.board[row][col] == self.board[row + 1][col + 1] and self.board[row][col] == self.board[row + 2][col + 2] and self.board[row][col] == self.board[row + 3][col + 3] and self.board[row][col] == self.board[row + 4][col + 4]:
                    self.gameOver = True

        if not self.gameOver:
            for row in range(0, ROW):
                for col in range(0, COL - 4):
                    if self.board[row][col] != 0 and self.board[row][col] == self.board[row][col + 1] and self.board[row][col] == self.board[row][col + 2] and self.board[row][col] == self.board[row][col + 3] and self.board[row][col] == self.board[row][col + 4]:
                        self.gameOver = True
                        break

        if not self.gameOver:
            for row in range(0, ROW - 4):
                for col in range(0, COL):
                    if self.board[row][col] == self.currentPlayer and self.board[row + 1][col] == self.currentPlayer and self.board[row + 2][col] == self.currentPlayer and self.board[row + 3][col] == self.currentPlayer and self.board[row + 4][col] == self.currentPlayer:
                        self.gameOver = True
                        break

        return self.gameOver

    def getPlayerMove(self):
        move = input('Player ' + str(self.currentPlayer) + ' Select a column (0-8): ')
        if self.checkCol(int(move)):
            return
        else:
            self.getPlayerMove()

    def changePlayer(self):
        if self.currentPlayer == PLAYER_1:
            self.currentPlayer = PLAYER_2
        else:
            self.currentPlayer = PLAYER_1


def main():
    print("Connect 5\nby Joe O'Regan\n")
    game = Game()
    continueGame = "y"

    while continueGame == "y":
        while not game.getGameOver():
            game.drawBoard()
            game.getPlayerMove()
            game.checkWin()
            if not game.getGameOver():
                game.changePlayer()

        game.drawBoard()
        print("Game Over! Player " + str(game.currentPlayer) + " Is The Winner!!!")

        continueGame = str(input("Play Again Y/N: "))
        if continueGame.lower() == "y":
            game = Game()
    print("\nThank You For Playing Connect 5 by Joe O'Regan. Goodbye!")


if __name__ == "__main__":
    main()
