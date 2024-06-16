# class Solution:
#     def revList(self,lst,s,e):
#         s=0
#         n=len(lst)
#         e=n-1
#         if s<e:
#              lst[s],lst[e] = lst[e],lst[s]
#              self.revList(lst,s+1,e-1)
       
       


# t1 = Solution()
# ls = [1,2,3,4,5]
# print(t1.revList(ls,0,len(ls)-1))
ls = [1,2,3,4,5]
print(ls.reverse())
