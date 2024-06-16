
class Solution:
    def convertToWords(self, n):
        ones=["","one ","two ","three ","four ","five ","six ","seven ","eight ","nine ","ten ","eleven ","twelve ","thirty ","fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
        tens=["","","twenty ","thirty ","fourty ","fifty ","sixty ","seventy ","eighty ","ninety"]

        def completeWord(n,s):
            ans = ""
            if n < 19:
                ans += ones[n]
            else:
                ans += tens[n//10] + ones[n%10]
            if n:
                ans += s       
            return ans
        
        output = ""
        output += completeWord((n//10000000),"crore ")
        output += completeWord((n//100000)%100,"lakh ")
        output += completeWord((n//1000)%100,"thousand ")
        output += completeWord((n//100)%10,"hundrad ")
        if(n > 100 and n % 100):
            output += "and "
        output += completeWord((n % 100), "")
        return output



t1 = Solution()
print(t1.convertToWords(655905))