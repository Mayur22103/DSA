def f1(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print(f1(151))
    