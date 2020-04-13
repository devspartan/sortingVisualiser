import pygame
import random


pygame.init()
def buildMaxHeap(list, size):
    len = int(size/2) - 1
    while len >= 0:
        maxHeapify(list, len, size)
        len -= 1

def maxHeapify(list, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < size and list[left].h < list[i].h:
        max = left
    if right < size and list[right].h < list[max].h:
        max = right
    if max != i:
        list = swap(list, i, max)
        maxHeapify(list, max, size)
        moveRectangle(list, i, max)

def swap(list, i, j):
    get = list[i], list[j]
    list[j], list[i] = get
    get = list[i].x, list[j].x
    list[j].x, list[i].x = get
    return list

def heapSort(list, size):
    buildMaxHeap(list, size)
    size -= 1
    while size:
        list = swap(list, 0, size)
        maxHeapify(list, 0, size)
        size -= 1
    moveRectangle(list, 0, 1)

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
        list[i].drawRectangle((255, 0, 0))
        list[j].drawRectangle((0, 0, 255))
        pygame.display.update()
        clock.tick(60)
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
size = 157
for i in range(size):
    numArr.append(random.randint(1, 980))
for i in range(size):
    list.append(Rectangle(20 + 10*i, 990, 5, -numArr[i]))

heapSort(list, size)

for i in range(size):
    print(list[i].h)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()