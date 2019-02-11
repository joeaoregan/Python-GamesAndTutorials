# Joe O'Regan
# 11/02/2019
# Connect 5 - PyGame

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
ROW, COL, PLAYER_1, PLAYER_2 = 6, 9, 1, 2
GREY, RED, GREEN, BLUE, TEXT_COLOUR = (125, 125, 125), (255, 0, 0), (0, 255, 0), (0, 0, 255), (200, 200, 200)  # Colours
COL_X, COL_Y, COL_W, COL_H, DISK_SIZE = 50, 60, 60, 360, 60
DISK_X, DISK_Y = int(COL_X + (DISK_SIZE / 2)), int(COL_Y + (DISK_SIZE / 2))

replayButton = (490, 430, 100, 40)


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


game = Game()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 24)
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Window Test")

mousePos = (0, 0)
selected = "Ready To Start"
moveText = "Player 1 Move"
run = True
while run:
    pygame.time.delay(100)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    # Draw Rects
    for i in range (0, 9):
        pygame.draw.rect(win, RED, (50 + (i * 60), COL_Y, COL_W, COL_H), 2)

    # Select Column and Highlight Selection
    for i in range(0,9):
        if not game.gameOver:
            if COL_Y < mousePos[1] < COL_Y + COL_H:
                if (COL_X + (DISK_SIZE * i)) < mousePos[0] < (COL_X + DISK_SIZE + (DISK_SIZE * i)):
                    pygame.draw.rect(win, GREEN, (COL_X + (i * COL_W), COL_Y, COL_W, COL_H), 0)    # highlight selected column
                    selected = "Player "+str(game.currentPlayer) + " Column Selected: " + str(i)

                    if game.checkCol(i):    # If the column isn't already full (a valid move)
                        if not game.checkWin():
                            game.changePlayer()
                            moveText = "Player " + str(game.currentPlayer) + " Move"
                        else:
                            selected = "Game Over. Player " + str(game.currentPlayer) + " Wins!"
                    else:
                        moveText = "Player " + str(game.currentPlayer) + " Move. Select A Different Column"
                    mousePos=(0, 0) # Reset move

                    break
                else:
                    selected = "Column Selected: None"
        else:
            if replayButton[1] < mousePos[1] < replayButton[1] + replayButton[3]:
                if replayButton[0] < mousePos[0] < replayButton[0] + replayButton[2]:
                    game = Game()
                    selected = "Ready To Start"
                    moveText = "Player " + str(game.currentPlayer) + " Move"

    if game.gameOver:
        moveText = "Thank Your For Playing"
        pygame.draw.rect(win, GREY, (replayButton[0], replayButton[1], replayButton[2], replayButton[3]), 0)
        font.set_bold(True)
        replayText = font.render("Replay", True, (225, 225, 225))
        win.blit(replayText,(replayButton[0]+8, replayButton[1]))
        font.set_bold(False)

    clickText = font.render(selected, False, TEXT_COLOUR)
    playerMoveText = font.render(moveText, False, TEXT_COLOUR)
    win.blit(clickText,(50,20))
    win.blit(playerMoveText,(50,430))

    # Draw Circles
    for r in range(0, ROW):
        for c in range(0, COL):
            if game.board[r][c] == 0:
                pygame.draw.circle(win, GREY, (DISK_X + (DISK_SIZE * c), DISK_Y + (DISK_SIZE * r)), 25)
            if game.board[r][c] == PLAYER_1:
                pygame.draw.circle(win, RED, (DISK_X + (DISK_SIZE * c), DISK_Y + (DISK_SIZE * r)), 25)
            if game.board[r][c] == PLAYER_2:
                pygame.draw.circle(win, BLUE, (DISK_X + (DISK_SIZE * c), DISK_Y + (DISK_SIZE * r)), 25)

    pygame.display.update()


pygame.quit()


"""
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
    
"""
