class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if(n>m) :
         return("greater")
        elif(n<m) :
         return("lesser")
        else :
         return("equal")
        

t1 = Solution()
print(t1.compareNM(4,8))