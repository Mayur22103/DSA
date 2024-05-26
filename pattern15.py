def nLetterTriangle(n: int):
    # Write your solution here.
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(chr(65+j),end=" ")
        print()



nLetterTriangle(5)