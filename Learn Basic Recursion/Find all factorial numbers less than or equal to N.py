class Solution:
    def factorialNumbers(self, N,i=1,sum=None):
        result = []
        i=1
        fact = 1
        while fact<=N:
            result.append(fact)
            i+=1
            fact*=i
        return result
    

t1 = Solution()
print(t1.factorialNumbers(300))
 