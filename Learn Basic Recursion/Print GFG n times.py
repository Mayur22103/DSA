class Solution:
    def printGfg(self, n,i=1):
        if(i>n):
            return
        print("GFG",end=" ")
        self.printGfg(n,i+1)


t1 = Solution()
t1.printGfg(5)
        

