def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    return False

max_num = 9999999
max_palindrome = 0

for i in range(max_num, 99, -1):
    for j in range(i, 99, -1):
        res = i * j
        
        if max_palindrome >= res:
            break
            
        if is_palindrome(res):
            max_palindrome = res
            
print(max_palindrome)