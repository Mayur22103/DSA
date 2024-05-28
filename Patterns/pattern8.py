def nStarTriangle(n: int) -> None:
    # Write your code here.
    k = n*2-1
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end="")
        for j in range(1,k+1):
            print("*",end="")
        print()
        k -= 2
        

nStarTriangle(7)