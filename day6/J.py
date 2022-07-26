n = int(input())
arr = list(map(int, input().split(' ')))
s = len(arr)

temp = 0
count = 0
best = 0

for i in range(s):
  if temp < arr[i]:
    count += 1
  else:
    count = 1

  best = max(best, count)
  temp = arr[i]

print(best)

