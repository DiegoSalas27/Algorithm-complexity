
# Find a given number in a sorted array with binary search
def binarySearch(left, right, array, value):
    
    if left > right:
        return False

    mid = int((left + right)/2)

    if array[mid] == value:
        return True
    
    if array[mid] > value:
        return binarySearch(left, mid - 1, array, value)
    else:
        return binarySearch(mid + 1, right, array, value)

# array = [1,2,3,4,5]
# print(binarySearch(0, len(array)-1, array, 3))

# Fibonacci O(n^2)

def Fibo(n):
    if n <= 1:
        return n
    else:
        return Fibo(n - 1) + Fibo(n - 2)
print(Fibo(5))

# Fibonacci with memoization (we trade time for space)

def FiboMemo(n, memo, memo2):
    if n <= 1:
        return n
    if memo2[n] == True:
        return memo[n]
    else:
        memo2[n] = True
        memo[n] = FiboMemo(n - 1, memo, memo2) + FiboMemo(n - 2, memo, memo2)
        return FiboMemo(n - 1, memo, memo2) + FiboMemo(n - 2, memo, memo2)

number = 5
memo2 = [False]*(number+1)
memo = [0]*(number+1)
print(FiboMemo(number, memo, memo2))

print(memo)

# Merge sort

def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0
    for k in range (first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)

def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)
    else:
        return print(A)

array2 = [1,2,3,4,9,2]
merge_sort(array2)