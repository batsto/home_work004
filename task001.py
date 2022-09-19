# 1 - Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


N = int(input())

def simple_factor(x):
    result = []
    i = 2
    while i <= x:
        if x%i == 0:
            result.append(i)
            x /= i
        else:
            i += 1
    return result

print(simple_factor(N))
        