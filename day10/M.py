import math

def isSquare(n):
    raiz = math.sqrt(n)
    return raiz*raiz == n

def solve(n):
    if n % 2 == 0 and isSquare(n/2):
        return 'YES'

    if n % 4 == 0 and isSquare(n/4):
        return 'YES'

    return 'NO'

t = int(input())
for i in range(t):
    print(solve(int(input())))
