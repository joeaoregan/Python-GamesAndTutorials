import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
ROW, COL, PLAYER_1, PLAYER_2 = 6, 9, 1, 2
GREY, RED, BLUE = (125,125,125), (255,0,0), (0,0,255)   # Colours
COL_Y, COL_W, COL_H = 60, 60, 360

replayButton = (490,430,100,40)


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


###############################################################################

game = Game()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 24)


# board = [[0 for col in range(COL)] for row in range(ROW)]   # init board to all 0's

win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Window Test")

pos1 = (0, 0)
selected = "Ready To Start"
moveText = "Player 1 Move"
run = True
while run:
    pygame.time.delay(100)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            move = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            pos1 = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    # Draw Rects
    for i in range (0, 9):
        pygame.draw.rect(win, (255,0,0), (50 + (i * 60), COL_Y, COL_W, COL_H), 2)

    ##coordSurface = font.render('Mouse Co-ordinates ' + str(move), False, (100,100,100))
    ##win.blit(coordSurface,(20,0))

    #if pos1 is not None:
    #   lastClicked = font.render('Mouse Clicked: ' + str(pos1), False, (100,100,100))
    #    win.blit(lastClicked,(20,50))

    # Select Column and Highlight Selection
    for i in range(0,9):
        if not game.gameOver:
            if 80 < pos1[1] < 440:
                if (50 + (60*i)) < pos1[0] < (110+(60*i)):
                    pygame.draw.rect(win, (0, 255, 0), (50 + (i * COL_W), COL_Y, COL_W, COL_H), 0)    # highlight selected column
                    selected = "Player "+str(game.currentPlayer) + " Column Selected: " + str(i)

                    if game.checkCol(i):    # If the column isn't already full (a valid move)
                        if not game.checkWin():
                            game.changePlayer()
                            moveText = "Player " + str(game.currentPlayer) + " Move"
                        else:
                            selected = "Game Over. Player " + str(game.currentPlayer) + " Wins!"
                    else:
                        moveText = "Player " + str(game.currentPlayer) + " Move. Select A Different Column"
                    pos1=(0,0) # Reset move

                    break
                else:
                    selected = "Column Selected: None"
        else:
            if replayButton[1] < pos1[1] < replayButton[1] + replayButton[3]:
                if replayButton[0] < pos1[0] < replayButton[0] + replayButton[2]:
                    game = Game()
                    selected = "Ready To Start"
                    moveText = "Player " + str(game.currentPlayer) + " Move"

    if game.gameOver:
        moveText = "Thank Your For Playing"
        pygame.draw.rect(win, GREY, (replayButton[0], replayButton[1], replayButton[2], replayButton[3]), 0)
        clickText = font.render("Replay", False, (200,200,200))
        win.blit(clickText,(replayButton[0]+10, replayButton[1]+5))

    clickText = font.render(selected, False, (200,200,200))
    playerMoveText = font.render(moveText, False, (200,200,200))
    win.blit(clickText,(50,20))
    win.blit(playerMoveText,(50,430))

    # Draw Circles
    for r in range(0, ROW):
        for c in range(0, COL):
            if game.board[r][c] == 0:
                pygame.draw.circle(win, GREY, (80 + (60 * c), COL_Y + 30 + (60 * r)), 25)
            if game.board[r][c] == 1:
                pygame.draw.circle(win, RED, (80 + (60 * c), COL_Y + 30 + (60 * r)), 25)
            if game.board[r][c] == 2:
                pygame.draw.circle(win, BLUE, (80 + (60 * c), COL_Y + 30 + (60 * r)), 25)


    pygame.display.update()


pygame.quit()
