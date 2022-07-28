line = input().split(' ')
a1 = int(line[0])
a2 = int(line[1])
changer = 0
minutes = 0

while a1 > 0 and a2 > 0:
    if a1 < a2:
        changer = 1
    else:
        changer = 2

    if a1 == 1 and changer == 2:
        break
    if a2 == 1 and changer == 1:
        break

    if changer == 1:
        a1 += 1
        a2 -= 2
    else:
        a1 -= 2
        a2 += 1

    minutes += 1

print(minutes)
