import pygame
import random


pygame.init()
speed = 50
size = 150
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def drawRectangle(self, color = (0, 240, 240)):
        pygame.draw.rect(display, color, [self.x, self.y, self.w, self.h])

def bubbleSort(list, size):
    for j in range(size):
        for i in range(size - j - 1):
            if list[i + 1].h > list[i].h:
                list = swap(list, i, i + 1)
                moveRectangleQuickBubbleHeapInsertion(list, i, i + 1)

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
            moveRectangleQuickBubbleHeapInsertion(list, i, j)
        j += 1
    quickSort(list, start, i - 1)
    quickSort(list, i + 1, end)

def insertionSort(list, size):
    for i in range(1, size):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j].h < key.h:
            list = swap(list, j+1, j)

            j -= 1
        moveRectangleQuickBubbleHeapInsertion(list, j + 1, j)

def heapSort(list, size):
    buildMaxHeap(list, size)
    size -= 1
    while size:
        list = swap(list, 0, size)
        maxHeapify(list, 0, size)
        size -= 1
    moveRectangleQuickBubbleHeapInsertion(list, 0, 1)

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
        moveRectangleQuickBubbleHeapInsertion(list, i, max)

def swap(list, i, j):
    get = list[i], list[j]
    list[j], list[i] = get
    get = list[i].x, list[j].x
    list[j].x, list[i].x = get
    return list

def mergeSort(list, start, end, startx, gapFactor):
    if start == end:
        return
    mid = int((start + end) / 2)
    mergeSort(list, start, mid, startx, gapFactor)
    mergeSort(list, mid + 1, end, startx, gapFactor)
    merge(list, start, mid, end)
    moveRectangleMergeSort(list, start, end, startx, gapFactor)


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

def moveRectangleMergeSort(list, i, j, startx, gapFactor, color = (255, 0, 0)):
    while i <= j:
        display.fill((235, 235, 235))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pauseSorting()

        mouseOperations()
        printRectangle(list)
        list[i].x = startx + gapFactor*i
        list[i].drawRectangle(color)
        i += 1
        pygame.display.update()
        clock.tick(speed)

def moveRectangleQuickBubbleHeapInsertion(list, i, j):
    while True:
        display.fill((235, 235, 235))
        printRectangle(list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pauseSorting()

        mouseOperations()
        list[i].drawRectangle((255, 0, 0))
        list[j].drawRectangle((0, 255, 0))
        pygame.display.update()
        clock.tick(speed)
        break

def mouseOperations():
    font1 = pygame.font.Font("comicbd.ttf", 20)
    font2 = pygame.font.Font("comicbd.ttf", 40)
    pygame.draw.rect(display, (150, 150, 150), [700, 965, 30, 30])
    minus = font2.render("-", True, (240, 240, 240))
    display.blit(minus, (703, 945))
    speedText = font1.render("Speed", True, (10, 10, 10))
    display.blit(speedText, (740, 965))
    pygame.draw.rect(display, (150, 150, 150), [810, 965, 30, 30])
    plus = font2.render("+", True, (240, 240, 240))
    display.blit(plus, (813, 947))
    pygame.draw.rect(display, (150, 150, 150), [10, 965, 60, 30])
    back = font1.render("Back", True, (240, 240, 240))
    display.blit(back, (17, 963))

    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()
    if 695 < mousePos[0] < 732 and 955 < mousePos[1] < 995:
        pygame.draw.rect(display, (110, 110, 110), [700, 965, 30, 30])
        display.blit(minus, (703, 945))
        decreaseSpeed()

    if 800 < mousePos[0] < 840 and 955 < mousePos[1] < 995:
        pygame.draw.rect(display, (110, 110, 110), [810, 965, 30, 30])
        display.blit(plus, (813, 947))
        increaseSpeed()

    if 7 < mousePos[0] < 70 and 960 < mousePos[1] < 995:
        pygame.draw.rect(display, (110, 110, 110), [10, 965, 60, 30])
        display.blit(back, (17, 963))
        if mouseClick[0] is 1:
            selectSize(size)

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

def increaseSpeed():
    global speed
    speed += 1
    if speed > 120:
        speed = 120

def decreaseSpeed():
    global speed
    speed -= 1
    if speed < 2:
        speed = 2

def sortCaller(size, key):
    numArr = []
    list = []
    gapFactor = 0
    width = 0
    global speed
    speed = 60
    if size <= 110:
        gapFactor = 14
        width = 7
    elif 110 < size <= 190:
        gapFactor = 8
        width = 4
    elif 190 < size <= 250:
        gapFactor = 6
        width = 3
    elif 250 < size <= 300:
        gapFactor = 5
        width = 3
    elif size > 300:
        gapFactor = 4
        width = 2
    startx = int((1600 - ((size-1)*gapFactor))/2)
    for a in range(size):
        numArr.append(random.randint(1, 940))
    for i in range(size):
        list.append(Rectangle(startx + i*gapFactor, 955, width, -(numArr[i])))
    if key is 1:
        bubbleSort(list, size)
    elif key is 2:
        quickSort(list, 0, size - 1)
    elif key is 3:
        insertionSort(list, size)
    elif key is 4:
        mergeSort(list, 0, size - 1, startx, gapFactor)
        moveRectangleMergeSort(list, 0, size-1, startx, gapFactor, (0, 255, 0))
    elif key is 5:
        heapSort(list, size)


def selectSize(size):
    while True:
        display.fill((217, 217, 217))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        size = displayText(size)

        pygame.display.update()
        clock.tick(30)

def displayText(size):
    font1 = pygame.font.Font("comic.ttf", 120)
    font2 = pygame.font.Font("comici.ttf", 60)
    font3 = pygame.font.Font("comici.ttf", 100)

    visualiser = font1.render("Sorting Algo Visualiser", True, (90, 90, 90))
    sizeOfArray = font2.render("Size of Array: " + str(size), True, (102, 102, 102))
    plus = font3.render("+", True, (255, 255, 255))
    minus = font3.render("-", True, (255, 255, 255))
    display.blit(visualiser, (150, 30))
    display.blit(sizeOfArray, (100, 250))
    pygame.draw.rect(display, (112, 112, 112), [650, 263, 60, 60])
    display.blit(minus, (655, 209))
    pygame.draw.rect(display, (112, 112, 112), [740, 263, 60, 60])
    display.blit(plus, (742, 214))

    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()

    if 645 < mousePos[0] < 710 and 250 < mousePos[1] < 323:
        pygame.draw.rect(display, (80, 80, 80), [650, 263, 60, 60])
        display.blit(minus, (655, 209))
        if mouseClick[0] is 1:
            size = sizeDecremnt(size)

    if 735 < mousePos[0] < 800 and 250 < mousePos[1] < 323:
        pygame.draw.rect(display, (80, 80, 80), [740, 263, 60, 60])
        display.blit(plus, (742, 214))
        if mouseClick[0] is 1:
            size = sizeIncremnt(size)

    bubbleSortText = font2.render("Bubble Sort", True, (102, 102, 102))
    quickSortText = font2.render("Quick Sort", True, (102, 102, 102))
    insertionSortText = font2.render("Insertion Sort", True, (102, 102, 102))
    mergeSortText = font2.render("Merge Sort", True, (102, 102, 102))
    heapSortText = font2.render("Heap Sort", True, (102, 102, 102))

    display.blit(bubbleSortText, (100, 370))
    display.blit(quickSortText, (100, 450))
    display.blit(insertionSortText, (100, 530))
    display.blit(mergeSortText, (100, 610))
    display.blit(heapSortText, (100, 690))

    if 110 < mousePos[0] < 440 and 390 < mousePos[1] < 440:
        bubbleSortText = font2.render("Bubble Sort", True, (80, 80, 80))
        display.blit(bubbleSortText, (100, 370))
        if mouseClick[0] is 1:
            sortCaller(size, 1)
            pygame.time.wait(1500)

    if 110 < mousePos[0] < 410 and 470 < mousePos[1] < 525:
        quickSortText = font2.render("Quick Sort", True, (80, 80, 80))
        display.blit(quickSortText, (100, 450))
        if mouseClick[0] is 1:
            sortCaller(size, 2)
            pygame.time.wait(1500)

    if 110 < mousePos[0] < 510 and 550 < mousePos[1] < 600:
        insertionSortText = font2.render("Insertion Sort", True, (80, 80, 80))
        display.blit(insertionSortText, (100, 530))
        if mouseClick[0] is 1:
            sortCaller(size, 3)
            pygame.time.wait(1500)

    if 104 < mousePos[0] < 420 and 625 < mousePos[1] < 690:
        mergeSortText = font2.render("Merge Sort", True, (80, 80, 80))
        display.blit(mergeSortText, (100, 610))
        if mouseClick[0] is 1:
            sortCaller(size, 4)
            pygame.time.wait(1500)

    if 102 < mousePos[0] < 390 and 705 < mousePos[1] < 765:
        heapSortText = font2.render("Heap Sort", True, (80, 80, 80))
        display.blit(heapSortText, (100, 690))
        if mouseClick[0] is 1:
            sortCaller(size, 5)
            pygame.time.wait(1500)

    return size


def sizeIncremnt(size):
    size += 2
    if size > 380:
        size = 380
    return size

def sizeDecremnt(size):
    size -= 2
    if size < 50:
        size = 50
    return size

display = pygame.display.set_mode((1600, 1000))
clock = pygame.time.Clock()
selectSize(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()