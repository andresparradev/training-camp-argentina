def solve(n, s, a):
    liters = 0
    a.sort()

    for i in range(n-1):
        liters += a[i]

    if liters <= s:
        return 'YES'

    return 'NO'


n, s = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
print(solve(n, s, a))

