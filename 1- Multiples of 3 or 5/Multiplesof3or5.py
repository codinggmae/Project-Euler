def sum_n(n, limit):
    k = (limit - 1) // n
    return n * k * (k + 1) // 2

sum = sum_n(3, 1000) + sum_n(5, 1000) - sum_n(15, 1000)
print(sum) 