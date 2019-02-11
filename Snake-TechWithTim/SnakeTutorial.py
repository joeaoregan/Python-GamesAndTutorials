# Snake-TechWithTim-TheNewBoston Tutorial Python
# https://www.youtube.com/watch?v=5tvER0MT14s&list=PLzMcBGfZo4-kQNQxlrgl5FtncvEbD0urc

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, colour=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    body = []
    turns = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x,y = 0,0
    for l in range(rows):
        x += sizeBetween
        y += sizeBetween

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))


def redrawWindow(win):
    global rows,width
    win.fill((0,0,0))
    drawGrid(width, rows, win)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass

def main():
    global width,rows
    width, height, rows = 500,500,20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)

    pass

main()
