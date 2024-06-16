def f1(n):
    sum = 0
    num = n
    while n > 0:
        ld = n % 10
        sum += ld ** 3
        n = n//10
    if sum == num:
        return True
    else:
        return False
        
print(f1(153))
            