def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    start = 1
    for i in range(1,n+1):
        if(i%2):
            start = 1
        else:
            start = 0
        for j in range(1,i+1):
            print(start,end=" ")
            start = 1 - start
        print()
      
nBinaryTriangle(5)