import pygame
import random


pygame.init()
def mergeSort(list, start, end):
    if start == end:
        return
    mid = int((start + end) / 2)
    mergeSort(list, start, mid)
    mergeSort(list, mid + 1, end)
    merge(list, start, mid, end)
    moveRectangle(list, start, end)

def merge(list, start, mid, end):
    tempList = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if list[i].h >= list[j].h:
            tempList.append(list[i])
            i += 1
        else:
            tempList.append(list[j])
            j += 1
    while i <= mid:
        tempList.append(list[i])
        i += 1
    while j <= end:
        tempList.append(list[j])
        j += 1
    var = 0
    for i in range(start, end + 1):
        list[i] = tempList[var]
        var += 1

def moveRectangle(list, i, j, color = (255, 0, 0)):
    while i <= j:
        display.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pauseSorting()

        printRectangle(list)
        list[i].x = 20 + 4 * i
        list[i].drawRectangle(color)
        print(list[i].h)
        i += 1

        pygame.display.update()
        clock.tick(80)

def printRectangle(list):
    for i in list:
        i.drawRectangle()

def pauseSorting():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return


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
    numArr.append(random.randint(1, 990))

for i in range(size):
    list.append(Rectangle(20 + 4*i, 990, 2, -numArr[i]))

mergeSort(list, 0, size-1)
moveRectangle(list, 0, size-1, (0, 255, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()