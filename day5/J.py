def solve(n):
    solutions = [
        'O-|-OOOO',
        'O-|O-OOO',
        'O-|OO-OO',
        'O-|OOO-O',
        'O-|OOOO-',
        '-O|-OOOO',
        '-O|O-OOO',
        '-O|OO-OO',
        '-O|OOO-O',
        '-O|OOOO-'
    ]
    numbers = [int(a) for a in str(n)]

    for i in numbers[::-1]:
        print(solutions[i])


n = int(input())
solve(n)
