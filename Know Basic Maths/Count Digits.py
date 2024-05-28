class Solution:
    def evenlyDivides (self, N):
        # code here
        n = N
        cnt = 0
        while(n > 0):
            rem = n%10
            if(rem != 0 and N%rem == 0):
                cnt += 1
            n = n//10
        return cnt
    
t1  = Solution()
print(t1.evenlyDivides(2246))
