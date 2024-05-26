class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        while x > 0:
            rem = x%10
            ans = ans*10+rem
            x = x//10
        return ans


t1= Solution()
print(t1.reverse(-98453))