import pygame
import random


pygame.init()

def insertionSort(list):
    for i in range(1, size):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j].h < key.h:
            list = swap(list, j+1, j)
            moveRectangle(list, j + 1, j)
            j -= 1

    return list

def swap(list, i, j):
    get = list[i], list[j]
    list[j], list[i] = get
    get = list[i].x, list[j].x
    list[j].x, list[i].x = get
    return list

def printRectangle(list):
    for i in list:
        i.drawRectangle()

def moveRectangle(list, i, j):
    while True:
        display.fill((255, 255, 255))
        printRectangle(list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        list[i].drawRectangle((0, 255, 0))
        list[j].drawRectangle((255, 0, 0))
        pygame.display.update()
        clock.tick(80)
        break

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def drawRectangle(self, color = (0, 255, 255)):
        pygame.draw.rect(display, color, [self.x, self.y, self.w, self.h])


display = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
numArr = []
list = []
size = 380
for i in range(size):
    numArr.append(random.randint(1, 1000))

for i in range(size):
    list.append(Rectangle(20 + 4*i, 990, 2, -numArr[i]))

list = insertionSort(list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()