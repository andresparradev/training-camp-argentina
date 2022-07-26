

import math

n = int(input())
word = input()
result = [""] * n

middle = word[0]
posMiddle = 0

if len(word) == 1:
    posMiddle = 0

if len(word) % 2 != 0:
    posMiddle = math.ceil(len(word)/2)-1
else:
    posMiddle = math.ceil(len(word)/2) - 1

result[posMiddle] = middle
j = posMiddle

h = 1
for i in range(1, n):
    if i % 2 != 0:
        if len(word) % 2 != 0:
            result[j-h] = word[i]
        else:
            result[j+h] = word[i]
    else:
        if len(word) % 2 != 0:
            result[j+h] = word[i]
        else:
            result[j-h] = word[i]
        h += 1

print("".join(result))
    
