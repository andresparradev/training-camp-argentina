def solve(n, s, firstTrack, secondTrack):
    r = firstTrack[0] == 1
    c = firstTrack[s-1] == 1

    h = False
    if s < n and (1 in firstTrack[s:n]):
        posUno = 0
        for i in range(n):
            if i >= s and firstTrack[i] == 1:
                posUno = i
                break
        
        if secondTrack[posUno] == 1 and secondTrack[s-1] == 1:
            h = True

    return r and (c or h)


firstLine = input().split(' ')
n = int(firstLine[0])
s = int(firstLine[1])

firstTrack = list(map(int, input().split(' ')))
secondTrack = list(map(int, input().split(' ')))

if solve(n,s,firstTrack,secondTrack):
    print('YES')
else:
    print('NO')


