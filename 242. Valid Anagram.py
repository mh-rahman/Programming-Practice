class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         dic = {}
#         for x,y in zip(s,t):
#             dic[x] = dic.get(x,0)+1
#             dic[y] = dic.get(y,0)-1
        
#         for i in dic.values():
#             if i!=0:
#                 return False
#         return True
        return Counter(s) == Counter(t)

        
        