from collections import Counter


def update_word(word):
    return 0


def split(word):
    return [char for char in word]


def exist_repetitions(arr):
    for i in arr.items():
        if i[1] != 1:
            return True
    return False


n = int(input())
word = input()
counts = {}
to_remove = 0

initial_ascii = 97
sequences = res = [word[i: j] for i in range(len(word))
                   for j in range(i + 1, len(word) + 1)]
repe = Counter(sequences)

if n == 1:
    print(-1)
else:
    while exist_repetitions(repe):
        word = "a" + word[1:len(word)]
        sequences = res = [word[i: j] for i in range(len(word))
                           for j in range(i + 1, len(word) + 1)]

        repe = Counter(sequences)

        print(sequences)
        print(repe)
