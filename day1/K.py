n = int(input())
count = 0

m = round(n/2)

for i in range(1, round(n/4)+1):
    if ((m-i)+(m-(m-i)) == m) and (m-i) != (m-(m-i)) and (m-i) > (m-(m-i)):
        print(str(i) + " - " + str(m-i) + ", " + str(m-(m-i)))
        count += 1
    else:
        break

print(count)
# result = round(round(n/2)/2) -1

# if result > 0:
#     print(result)
# else:
#     print(0)

