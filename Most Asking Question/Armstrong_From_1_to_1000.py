def f1():
  
    for i in range(1,1001):
        num = i
        n = len(str(i))
        sum = 0
        i = str(i)
        for digit in i:
            sum += int(digit) ** n
        if sum == num:
            print(sum)
       
        
print(f1())
            


   