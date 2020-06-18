class Solution:
    def hIndex(self, c: List[int]) -> int:
        
        return max([min(len(c)-i,n) for i,n in enumerate(c)]) if c else 0

#         rank = 0
#         l = len(c)
#         for i in range(l):
#             temprank = min(l-i,c[i])
#             rank = max(rank,temprank)
            
#         return rank
