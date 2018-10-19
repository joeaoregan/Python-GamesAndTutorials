# PyGameTutorials
# Tutorial #8: Scoring and Health Bars
# https://www.youtube.com/watch?v=JLUqOmE9veI&index=8&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5

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

score = 0

BLACK = (0,0,0,255)


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
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 28, 52)

    def draw(self, win):
        if (self.walkCount + 1) > 27:
            self.walkCount = 0

        # walking right or left
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))   # integer divide excludes remainder or decimal place
                self.walkCount += 1
            elif man.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        # standing and looking right or left
        else:
            #win.blit(char, (self.x, self.y))
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 28, 52)     # update the hitbox position
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)  # draw hitbox


class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour=colour
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('Art/R1E.png'), pygame.image.load('Art/R2E.png'), pygame.image.load('Art/R3E.png'), pygame.image.load('Art/R4E.png'), pygame.image.load('Art/R5E.png'), pygame.image.load('Art/R6E.png'), pygame.image.load('Art/R7E.png'), pygame.image.load('Art/R8E.png'), pygame.image.load('Art/R9E.png'), pygame.image.load('Art/R10E.png'), pygame.image.load('Art/R11E.png')]
    walkLeft = [pygame.image.load('Art/L1E.png'), pygame.image.load('Art/L2E.png'), pygame.image.load('Art/L3E.png'), pygame.image.load('Art/L4E.png'), pygame.image.load('Art/L5E.png'), pygame.image.load('Art/L6E.png'), pygame.image.load('Art/L7E.png'), pygame.image.load('Art/L8E.png'), pygame.image.load('Art/L9E.png'), pygame.image.load('Art/L10E.png'), pygame.image.load('Art/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            # health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)     # update hitbox
           # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)   # draw hitbox

    def move(self):
        if self.vel > 0:
            if self.x + self. vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health-=1
        else:
            self.visible = False
        print('hit')
        pass


def redrawGameWindow():
    win.blit(bg, (0,0))                                     # draw background
    text = font.render('Score: ' + str(score), 1, (0,0,0))  # black score text
    win.blit(text, (screenWidth - 120, 10))                 # draw score text in top right corner of screen
    man.draw(win)                                           # draw player
    goblin.draw(win)                                        # draw enemy
    for bullet in bullets:                                  # draw all bullets in list
        bullet.draw(win)

    pygame.display.update()


# main loop
font = pygame.font.SysFont('comicsans', 30, True)     # bold
man = player(200, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)  # FPS set to 27

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        # bullet collisions
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x - bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1  # increment score
                bullets.pop(bullets.index(bullet))

        # move bullets
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), 6, BLACK, facing))

        shootLoop = 1

    # keyboard movement
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left, man.right = True, False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.right, man.left = True, False
        man.standing = False
    else:
        man.standing = True
        # man.right, man.left = False, False    # if these are reset we won't know what way player was looking
        man.walkCount = 0

    if not man.isJump:
        # if keys[pygame.K_SPACE]:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right, man.left = False, False
            man.walkCount = 0
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
