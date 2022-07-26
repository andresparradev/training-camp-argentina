def solve(x, y, s):
    myX = 0
    myY = 0
    r = 0
    l = 0
    u = 0
    d = 0
    
    for i in s:
        if i == 'L':
            myX -= 1
            l += 1
        elif i == 'R':
            myX += 1
            r += 1
        elif i == 'U':
            myY += 1
            u += 1
        elif i == 'D':
            myY -= 1
            d += 1

    if x == myX and y == myY:
        return 'YES'

    yesX = False
    yesY = False
    for i in range(len(s)):
        if r-l == x:
            yesX = True
        
        if u-l == y:
            yesY = True

        r -= 1
        u -= 1

    if yesY and yesX:
        return 'YES'
    
    return 'NO'


n = int(input())

for i in range(n):
    line = input().split(' ')
    x = int(line[0])
    y = int(line[1])
    s = input()

    print(solve(x,y,s))
