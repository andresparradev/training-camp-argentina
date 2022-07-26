def solve(k):
    digits = len(str(k))
    n = int(str(k)[0])
    count = 0
    
    if k != 1:
        for i in range(n-1):
            count += 10
 
        for i in range(0, digits):
            count += (i+1)
    else:
        count = 1
 
    return count
 
 
n = int(input())
result = []
 
for i in range(n):
    k = int(input())
    result.append(solve(k))
 
 
for i in result:
    print(i)
