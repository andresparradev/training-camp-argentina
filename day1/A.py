def solve(names):
    result = []

    for i in range(len(names)):
        splitList = names[:i]
        if names[i] in splitList:
            result.append("YES")
        else:
            result.append("NO")
    
    for i in result:
        print(i)


n = int(input())
names = []

for i in range(n):
    names.append(input())


solve(names)
