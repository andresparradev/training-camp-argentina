def sum_list(list):
    aux = ''
    for n in list:
        aux += str(n)
    return int(aux)

def solve(number):
    digits = [int(a) for a in str(number)]

    if number%8 == 0:
        print('YES')
        print(number)
        return

    for i in range(len(digits)):
        if digits[i] % 8 == 0:
            print('YES')
            print(digits[i])
            return

    
    while(len(digits) > 1):
        digits.pop()
        if sum_list(digits)%8 == 0:
            print('YES')
            print(sum_list(digits))
            return


    print('NO')


n = int(input())
solve(n)
