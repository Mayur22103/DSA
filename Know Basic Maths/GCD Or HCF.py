
class Solution:
    def lcmAndGcd(self, A , B) :
        gcd = 1
        x = min(A,B)
        for i in range(x,1,-1):
            if(A%i == 0 and B%i == 0):
                gcd = i
                break
        lcm = (A*B) // gcd
        return lcm,gcd


t1 = Solution()
print(t1.lcmAndGcd(5,10))

