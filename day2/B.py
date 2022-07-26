def solve(n, k, matriz):
    counts = []

    for i in range(k):
        count = 0
        for j in range(n):
            if j < n-1 and matriz[i][j]+1 == matriz[i][j+1]:
                count += 1
        counts.append(count)

    counts.sort()
    count = counts[len(counts)-1]
    if count > 0:
        count += 1

    return count


firstLine = input().split(' ')
n = int(firstLine[0])
k = int(firstLine[1])
matriz = []

for i in range(k):
    listNumbers = list(map(int, input().split(' ')))
    matriz.append(listNumbers)

print(solve(n, k, matriz))
