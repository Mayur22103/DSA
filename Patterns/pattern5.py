def seeding(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        for j in range(n+1,i,-1):
            print("*",end=" ")
        print()

seeding(5)