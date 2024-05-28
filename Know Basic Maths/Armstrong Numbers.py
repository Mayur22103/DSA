class Solution:
    def armstrongNumber (self, n):
        k = len(str(n))
        sum = 0
        num = n
        
        while num > 0:
            ld = num%10
            sum += ld ** k
            num = num//10
            
        if(sum == n):
            return "Yes"
        else:
            return "No"
        

t1 = Solution()
print(t1.armstrongNumber())