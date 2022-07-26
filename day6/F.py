n = int(input())
count_goods = 0

for i in range(n):
  inputs = input().split(' ')
  name = inputs[0]
  pointsBefore = int(inputs[1])
  pointsAfter = int(inputs[2])

  if pointsBefore >= 2400 and pointsAfter > pointsBefore:
      count_goods += 1

if count_goods == 0:
  print('NO')
else:
  print('YES')
