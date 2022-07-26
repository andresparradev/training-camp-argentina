def split(word):
    return [char for char in word]
 
n = int(input())
word = split(input())
 

def main():
    counts = {}
    to_remove = 0
    initial_ascii = 97

    if n == 1:
        return -1
    else:
        i = 0
     
        for w in word:
            if w in counts:
                counts[w] += 1
                
                if counts[w] > 26:
                    return -1
     
                if initial_ascii == 122:
                    initial_ascii = 97
     
                chara = str(chr(initial_ascii))
     
                if chara != w and not(chara in counts):
                    word[i] = chara
                else:
                    word[i] = str(chr(initial_ascii+1))
     
                initial_ascii += 1
                to_remove += 1
            else:
                counts[w] = 1
     
            i += 1
     
     
        return to_remove

print(main())
