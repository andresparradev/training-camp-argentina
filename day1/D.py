line = input().split(' ')
n = int(line[0])
m = int(line[1])
minFriends = 0
maxFriends = 0
minTeams = [0] * m
maxTeams = [0] * m


if m != 1:
    r = n
    while r > 0:
        for i in range(m):
            if r > 0:
                minTeams[i] += 1
                r -= 1

    r = n
    while r > 0:
        for i in range(m):
            if r > 0:
                if maxTeams[i] == 0:
                    maxTeams[i] += 1
                else:
                    maxTeams[0] += 1
                r -= 1


    while n > 0:
        for i in range(m):
            if minTeams[i] >= 2:
                minFriends += 1
                minTeams[i] -= 2

            n -= 1

    maxFriends = 1
    for i in range(1, maxTeams[0]):
        maxFriends *= i


else:
    minFriends = n * 2
    maxFriends = minFriends

print(str(minFriends) + " " + str(maxFriends))
