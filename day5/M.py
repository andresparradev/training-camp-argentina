def get_max(dict):
    items_sorted = sorted(dict)
    val = dict[items_sorted[0]][0] - dict[items_sorted[0]][1]
    j = items_sorted[0]

    for i in range(1, len(items_sorted)):
        if (dict[items_sorted[i]][0] - dict[items_sorted[i]][1]) > val:
            j = items_sorted[i]
            val = dict[items_sorted[i]][0] - dict[items_sorted[i]][1] 

    return j


def solve(a, list_a, b, list_b):
    dict = {}

    for i in list_a:
        c = 0

        for j in range(a):
            if list_a[j] >= i:
                c += 3
            else:
                c += 2

        dict[i] = [c]

        k = 0
        for j in range(b):
            if list_b[j] >= i:
                k+=3
            else:
                k+=2

        dict[i] = dict[i] + [k]

    
    result = dict[get_max(dict)]
    return str(result[0])+":"+str(result[1])


a = int(input())
list_a = list(map(int, input().split(' ')))
b = int(input())
list_b = list(map(int, input().split(' ')))
print(solve(a, list_a, b, list_b))
