# https://www.youtube.com/watch?v=iLL2V1es52I&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
# up to part 17/100

import pygame, time, random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_SIZE = 10
FPS = 20

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game Tutorial')
pygame.display.update()

font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()


def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [(SCREEN_WIDTH / 2 - screen_text.get_width()/2), SCREEN_HEIGHT / 2])


def gameLoop():
    gameExit = False
    gameOver = False
    lead_x, lead_y = 300, 300
    lead_x_change, lead_y_change = 0, 0

    randAppleX = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE)
    randAppleY = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE)
    round(randAppleX/10.0) * 10.0   # round apple coords to match the snakes range
    round(randAppleY/10.0) * 10.0

    while not gameExit:
        while gameOver:
            gameDisplay.fill(WHITE)
            message_to_screen("Game over, press C to play again or Q to quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change == 0:
                    # lead_x -= BLOCK_SIZE
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and lead_x_change == 0:
                    # lead_x += BLOCK_SIZE
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0

                if event.key == pygame.K_UP and lead_y_change == 0:
                    # lead_y -= BLOCK_SIZE
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and lead_y_change == 0:
                    # lead_y += BLOCK_SIZE
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT
            #         lead_x_change = 0

        # if lead_x > SCREEN_WIDTH or lead_x < 0 or lead_y > SCREEN_HEIGHT or lead_y < 0:
        #     gameExit = True
        if lead_x > SCREEN_WIDTH:
            lead_x = 0
            # gameExit = True
            gameOver = True
        elif lead_x < -BLOCK_SIZE:
            lead_x = SCREEN_WIDTH

        if lead_y > SCREEN_HEIGHT:
            lead_y = 0
        elif lead_y < -BLOCK_SIZE:
            lead_y = SCREEN_HEIGHT

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(WHITE)
        # pygame.draw.rect(gameDisplay, BLACK, [400,300,10,10])
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            print("om nom nom")


        clock.tick(FPS)

    # message_to_screen("You Lose", RED)
    # pygame.display.update()
    #
    # time.sleep(2)
    pygame.quit()  # quit, and uninitialise
    quit()


gameLoop()
