class Solution:
    def dataTypeSize(self, str):
        sizes = {
            'Character' : 1,
            'Integer' : 4,
            'Long' : 8,
            'Float' : 4,
            'Double' : 8
        }
        return sizes[str]
        
        # if(str=="Character"):
        #     return 1
        # elif(str=="Float" or str=="Integer"):
        #     return 4
        # elif(str=="Long" or str=="Double"):
        #     return 8
        # else:
        #     return -1
        
        # Code here

t1 = Solution()
print(t1.dataTypeSize("Float"))
