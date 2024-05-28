class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        X = x
        while X > 0:
            rem = X % 10
            ans = ans*10+rem
            X = X//10
        return ans == x
    
t1= Solution()
print(t1.isPalindrome(1212))