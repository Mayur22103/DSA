class Solution:
    def printNos(self, n):
        if(n<1):
            return
        print(n,end=" ")
        self.printNos(n-1)



t1 = Solution()
t1.printNos(5)