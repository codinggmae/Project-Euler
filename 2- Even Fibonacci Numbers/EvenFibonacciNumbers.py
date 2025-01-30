def sumFibonachi(limit):
    f1 = 2
    f2 = 8
    sum = f1 + f2
    while True:
        next_f = 4 * f2 + f1
        if next_f > limit:
            break
        sum += next_f
        f1, f2 = f2, next_f
        
    return sum

print(sumFibonachi(4000000))