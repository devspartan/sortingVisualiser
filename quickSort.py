import pygame
import random


pygame.init()

def quickSort(list, start, end):
    if start > end:
        return
    pivot = list[end].h
    i = start - 1
    j = start
    while j <= end:
        if list[j].h >= pivot:
            i += 1
            list = swap(list, i, j)
            swapRectangle(list, i, j)
        j += 1
    quickSort(list, start, i - 1)
    quickSort(list, i + 1, end)

def swap(list, i, j):
    get = list[i], list[j]
    list[j], list[i] = get
    get = list[i].x, list[j].x
    list[j].x, list[i].x = get
    return list

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def drawRectangle(self, color = (0, 255, 255)):
        pygame.draw.rect(display, color, [self.x, self.y, self.w, self.h])

def printRectangle(list):
    for i in list:
        i.drawRectangle()

def swapRectangle(list, i, j):
    while True:
        display.fill((255, 255, 255))
        printRectangle(list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        list[j].drawRectangle((255, 0, 0))
        list[i].drawRectangle((0, 255, 0))
        pygame.display.update()
        clock.tick(speed)
        break

def moveRectangle(list, i, j):
    while i <= j:
        display.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        printRectangle(list)
        list[i].x = 20 + 4*i
        list[i].drawRectangle((255, 0, 0))
        print(list[i].h)
        i += 1
        pygame.display.update()
        clock.tick(speed)

display = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
numArr = []
list = []
speed = 10
size = 380
for i in range(size):
    numArr.append(random.randint(10, 990))

for i in range(size):
    list.append(Rectangle(20 + 4*i, 990, 2, -numArr[i]))

list = quickSort(list, 0, size - 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()