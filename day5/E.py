t = input()
s_begin = input()
s_end = input()
string = ''

if s_begin[len(s_begin)-1] == s_end[0]:
    string = s_begin[:len(s_begin)-1]
    string += s_end
else:
    string = s_begin+s_end

print(t.count(string))
