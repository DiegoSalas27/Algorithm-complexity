#backtracking also called exhaustive search

#Binary Strings O(n*2^2)

def BString(i, n, array):
    if i == n:
        print(array)
        return
    else:
        array[i] = 1
        BString(i + 1, n, array)

        array[i] = 0
        BString(i + 1, n, array)
size = 3
array = [-1]*size
# BString(0 , size, array)

#K-Ary strings O(n*k^n)

def kAry(i , n, array, basket):
    if i == n:
        print(array)
        return
    else:
        for x in range(len(basket)):
            array[i] = basket[x]
            kAry(i + 1, n, array, basket)
basket = ['a', 'b', 'c']
array = [-1]*(len(basket))
# kAry(0, len(basket), array, basket)

#Maze Problem: A rat need to get to the bottom right of a grid from the top left of the grid, it can go only down or right

def MazeRat(i, j, m, n, Maze, CMaze):
    for x in range(m):
        print('\n')
        for y in range(n):
            print(Maze[x][y], end = " ") 
    print('\n')
    if i < 0 or j < 0 or i == m or j == n:
        return 0
    if Maze[i][j] == -1:
        return 0
    if i == m - 1 and j == n - 1:
        for x in range(m):
            for y in range(n):
                Maze[x][y] = CMaze[x][y]
        return 1
    Maze[i][j] = 2
    a = MazeRat(i + 1, j, m, n, Maze, CMaze)
    b = MazeRat(i, j + 1, m, n, Maze, CMaze)

    return a + b

Maze = [[0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0]]

CMaze = [[0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0]]
# print(MazeRat(0, 0, 4, 4, Maze, CMaze))

# Gold Collector

def collect(i, n, array):
    if i >= n:
        return 0
    a = collect(i + 1, n, array)
    b = collect(i + 2, n, array) + array[i]
    print('i:', i, 'a:', a, 'b:', b)
    if a > b:
        return a
    else:
        return b

# array = [33,10,20,5,14,26]        
# print(collect(0, len(array), array))

# Rat Maze problem evolution

def MazeRat2(i, j, m, n, Maze2, CMaze2):
    for x in range(m):
        print('\n')
        for y in range(n):
            print(Maze2[x][y], end = " ") 
    print('\n')
    if i < 0 or j < 0  or i == m or j == n:
        return 0
    if Maze2[i][j] < 0:
        return 0
    if Maze2[i][j] == 2:
        return 1
    Maze2[i][j] = -1

    a = MazeRat2(i + 1, j, m, n, Maze2, CMaze2)
    b = MazeRat2(i, j + 1, m, n, Maze2, CMaze2)
    c = MazeRat2(i, j - 1, m , n, Maze2, CMaze2)
    d = MazeRat2(i - 1, j, m, n, Maze2, CMaze2)

    Maze2[i][j] = 0

    return a + b + c + d

Maze2 = [[0, 0, 0],
        [0, -1, 0],
        [0, -1, 2]]

CMaze2 = [[0, 0, 0],
        [0, -1, 0],
        [0, -1, 2]]

# print(MazeRat2(0, 0, 3, 3, Maze2, CMaze2))

def KnightProblem(i, j, n , m, Maze3, CMaze3):
    for x in range(m):
        print('\n')
        for y in range(n):
            print(Maze3[x][y], end = " ") 
    print('\n')
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if Maze3[i][j] == -1:
        return  0
    if Maze3[i][j] == 1:
        return 1
    Maze3[i][j] = -1

    a =KnightProblem(i + 2, j + 1, n , m, Maze3, CMaze3)
    b =KnightProblem(i + 2, j - 1, n , m, Maze3, CMaze3)
    c =KnightProblem(i + 1, j + 2, n , m, Maze3, CMaze3)
    d =KnightProblem(i + 1, j - 2, n , m, Maze3, CMaze3)
    e =KnightProblem(i - 2, j + 1, n , m, Maze3, CMaze3)
    f =KnightProblem(i - 2, j - 1, n , m, Maze3, CMaze3)
    g =KnightProblem(i - 1, j + 2, n , m, Maze3, CMaze3)    
    h =KnightProblem(i - 1, j - 2, n , m, Maze3, CMaze3)

    Maze3[i][j] = 0

    return a + b + c + d + e + f + g + h

Maze3 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 1]]

CMaze3 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 1]]

print(KnightProblem(0, 0, 3, 3, Maze3, CMaze3))