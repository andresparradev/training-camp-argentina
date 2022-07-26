def solve(password, words):
    result = 'NO'
    
    if len(words) == 1 and password in (words[0]*4):
        return 'YES'

    for i in range(len(words)):
        for j in range(len(words)):

            if i != j and password in (words[i]*2 + words[j]*2):
                return 'YES'

    return result

password = input()
n = int(input())
words = []

for i in range(n):
    words.append(input())

print(solve(password, words))
