import itertools

def get_subs(string):
    size = len(string)
    subs = []

    for i in range(1, size+1):
        s = list(itertools.combinations(string, i))
        for j in s:
            subs.append(''.join(j))

    return subs

a = input()
b = input()

def main():
    if len(a) >= len(b):
        subs = get_subs(a)
        
        for sub in reversed(subs):
            if (sub in b) == False:
                return len(sub)
    else:
        subs = get_subs(b)

        for sub in reversed(subs):
            if (sub in a) == False:
                return len(sub)

    return -1

print(main())
