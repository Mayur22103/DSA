class Solution:
    def printNos(self,N):
            #Your code here
        if N == 0:   
            return
        self.printNos(N-1)
        print(N,end=" ")

t1 = Solution()
t1.printNos(5)