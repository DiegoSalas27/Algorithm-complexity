#N Reinas

def draw(array):
    n = len(array)
    print('%s+'%('+---'*n))
    for i in range(n):
        s = '|'
        for j in range(n):
            s += ' %c |' % ('Q' if array[j] == i else ' ')
        print(s)
        print('%s+'%('+---'*n))
draw([0,1,2,3,4])