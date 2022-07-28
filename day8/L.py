def get_smallest_divisor(n):
    if n % 2 == 0:
        return 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i+=2

    return n


n = int(input())
count_subtrations = 0

while n != 0:
    smallest = get_smallest_divisor(n)
    n -= smallest
    count_subtrations += 1

print(count_subtrations)
