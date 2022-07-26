def solve(n, exercises):
    biceps=0
    back=0
    chest=0
    
    i = 1
    for exercise in exercises:
        if i == 1:
            chest += exercise
        elif i == 2:
            biceps += exercise
        elif i == 3:
            back += exercise

        if i == 3:
            i = 1
        else:
            i+=1

    if biceps > back and biceps > chest:
        return 'biceps'
    elif back > biceps and back > chest:
        return 'back'
    else:
        return 'chest'

n = int(input())
exercises = list(map(int, input().split(' ')))
print(solve(n, exercises))
