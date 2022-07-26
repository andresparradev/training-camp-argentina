def solve(n, m, notes):
    count = 0
 
    for note in notes:
        count += note
 
    if count >= m:
        return m
    
    return count
    
 
t = int(input())
result = []
 
for i in range(t):
    line = input().split(' ')
    n = int(line[0])
    m = int(line[1])
    notes = list(map(int, input().split(' ')))
    result.append(solve(n, m, notes))
 
 
for el in result:
    print(el)
