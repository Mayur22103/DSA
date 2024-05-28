class Solution:
    def isPrime (self, N):
        cnt = 0
        for i in range(1,N+1):
            if(N%i == 0):
                cnt += 1
        if(cnt == 2):
            return 1
        else:
            return 0
        
import math

# class Solution:
#     def isPrime(self, N):
#         # Check if N is less than 2
#         if N < 2:
#             return 0

#         # Loop from 2 to the square root of N
#         for i in range(2, int(math.sqrt(N)) + 1):
#             # If N is divisible by i, it's not prime
#             if N % i == 0:
#                 return 0

#         # If we haven't found any divisor, N is prime
#         return 1

t1 = Solution()
print(t1.isPrime(25))


