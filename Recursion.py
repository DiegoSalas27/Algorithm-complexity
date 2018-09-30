#Factorial

def Factorial(n):
    if n <= 1:
        return 1
    else:
        return n * Factorial(n - 1)
# print(Factorial(2))

# Find sum of numbers from 1 to n

def sumOneToN(n):
    if n <= 1:
        return n
    else:
        return n + sumOneToN(n - 1)
# print(sumOneToN(6))

# Check if a 1D array is symmetric

def symmetricA(left, right, array):
    if left >= right:
        return True
    elif array[left] != array[right]:
        return False
    else:
        return symmetricA(left + 1, right - 1, array)

# print(symmetricA(0, 4, [2,2,1,2,2]))

# The 3n + 1 Problem

def threen(n):
    print(n)
    if n == 1:
        return
    elif n % 2 != 0:
        n = 3 * n + 1
    else:
        n = n/2
    threen(n)
# threen(9)

# floodIsland

def floodFill(Matrix, x, y, m, n):

    print("[ ")
    for i in range(m):
        print("\n")
        for j in range(n+1):
            print(Matrix[i][j], end =" ")

    print("] \n")
    if x < 0 or y < 0 or x > n or y > m or Matrix[y][x] == 0:
        
        return
    else:
        Matrix[y][x] = 0

        floodFill(Matrix, x - 1, y, m, n)
        floodFill(Matrix, x, y - 1, m, n)
        floodFill(Matrix, x + 1, y, m, n)
        floodFill(Matrix, x, y + 1, m, n)

Matrix = [[1,1,1,0],
          [0,1,1,1],
          [1,0,1,0],
          [0,0,1,1]]

# floodFill(Matrix, 0, 0, 3, 3)
# print(Matrix)

