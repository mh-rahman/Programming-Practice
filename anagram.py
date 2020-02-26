class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic = {}
        for x,y in zip(s,t):
            dic[x] = dic.get(x,0)+1
            dic[y] = dic.get(y,0)-1
        
        for i in dic.values():
            if i!=0:
                return False
        return True
        
        
        
#         if len(s)!=len(t):
#             return False
        
#         s = sorted(list(s))
#         t = sorted(list(t))
        
#         for i,x in enumerate(s):
#             if x!=t[i]:
#                 return False
#         return True
        
        # print(t,s)
        # for x in s:
        #     if x not in t:
        #         return False
        #     else:
        #         t.remove(x)
        # if not t:
        #     return True
        # else:
        #     return False
        