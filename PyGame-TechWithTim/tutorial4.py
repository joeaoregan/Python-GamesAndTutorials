# PyGame-TechWithTim
# Tutorial #4: Optimisation & OOP
# https://www.youtube.com/watch?v=xfnRywBv5VM&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=4

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

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if (self.walkCount + 1) > 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))   # integer divide excludes remainder or decimal place
            self.walkCount += 1
        elif man.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


'''
x, y = 50, 400  # move down the screen
width, height = 64, 65
vel = 5
isJump = False
jumpCount = 10
left, right = False, False
walkCount = 0
'''


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0)) # draw back ground

    man.draw(win)

    pygame.display.update()


# main loop
man = player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)  # FPS set to 27

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # keyboard movement
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left, man.right = True, False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.right, man.left = True, False
    else:
        man.right, man.left = False, False
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right, man.left = False, False
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg   # change to get more realistic jump
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
