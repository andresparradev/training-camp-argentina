m = input()
l = int(input())
word = m

for i in range(l):
    x = int(input())
    suf = word[:x][::-1]
    pre = word[x:len(word)][::-1]
    word = suf + pre

print(word)
