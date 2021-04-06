#!/usr/bin/env python3

'''
Task 7
Develop a procedure that will have a size argument and print a table where num of columns and rows will be of this size. 
Cells of table should contain numbers from 1 to n ** 2 placed in a spiral fashion. 
Spiral should start from top left cell and has a clockwise direction (see the example below).

1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

def spiral():
    N = int(input("Please, input a size argument:"))
    
    # создаем список состоящий из списков (матрицу), который потом будем заполнять
    a = [None] * N
    for i in range(N): a[i] = [None] * N
    
    #начальные координаты
    x = 0
    y = 0
    
    # эти переменные задают движение по матрице.
    dx = 1
    dy = 0
    
    #заполнение матрицы
    for i in range(N * N):
        a[y][x] = i + 1
        ts = x + dx if dx else y + dy
        if ts < 0 or ts == N or a[y + dy][x + dx] != None:
            dx, dy = -dy, dx
        x += dx
        y += dy
    
    #вывод матрицы
    for y in range(N): print(a[y])

spiral()
