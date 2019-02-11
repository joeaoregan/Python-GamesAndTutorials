# PyGame-TechWithTim
# Tutorial #3: Character Animation and Sprites
# https://www.youtube.com/watch?v=UdsNBIzsmlI&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=3

import pygame
pygame.init()

screenWidth, screenHeight = 640, 480
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")

# Lists for left and right walking (could be flipped)
walkRight = [pygame.image.load('Art/R1.png'), pygame.image.load('Art/R2.png'), pygame.image.load('Art/R3.png'), pygame.image.load('Art/R4.png'), pygame.image.load('Art/R5.png'), pygame.image.load('Art/R6.png'), pygame.image.load('Art/R7.png'), pygame.image.load('Art/R8.png'), pygame.image.load('Art/R9.png')]
walkLeft = [pygame.image.load('Art/L1.png'), pygame.image.load('Art/L2.png'), pygame.image.load('Art/L3.png'), pygame.image.load('Art/L4.png'), pygame.image.load('Art/L5.png'), pygame.image.load('Art/L6.png'), pygame.image.load('Art/L7.png'), pygame.image.load('Art/L8.png'), pygame.image.load('Art/L9.png')]
bg = pygame.image.load('Art/bg.jpg')
char = pygame.image.load('Art/standing.png')

clock = pygame.time.Clock()     # clock variable to set FPS

x, y = 50, 400  # move down the screen
width, height = 64, 65
vel = 5
isJump = False
jumpCount = 10
left, right = False, False
walkCount = 0


def redrawGameWindow():
    global walkCount
    # win.fill((0,0,0))
    win.blit(bg, (0,0)) # draw back ground
    # pygame.draw.rect(win, (255,0,0), (x,y,width,height))

    if (walkCount + 1) > 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))   # integer divide excludes remainder or decimal place
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


# main loop
run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)  # FPS set to 27

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # keyboard movement
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left, right = True, False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right, left = True, False
    else:
        right, left = False, False
        walkCount = 0

    if not(isJump):
        '''
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel
        '''
        if keys[pygame.K_SPACE]:
            isJump = True
            right, left = False, False
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg   # change to get more realistic jump
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()
