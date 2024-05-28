def nStarTriangle(n: int) -> None:
    # Write your code here.
    k=1
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(" ",end="")
        for k in range(1,k+1):
            print("*",end="")
        k += 2
        print()


nStarTriangle(5)