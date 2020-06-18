class Solution:
    def hIndex(self, c: List[int]) -> int:
        
        #One liner
        return max([min(len(c)-i,n) for i,n in enumerate(c)]) if c else 0
        
        ##Linear time approach
#         l = len(c)
#         for i in range(l):
#             # print(i)
#             temprank = min(l-i,c[i])
#             if temprank < rank:
#                 break
#             else:
#                 rank = temprank
            
#         return rank


    ##Attempted log(N) approach
#         rank = 0
#         l = len(c)
#         li = 0
#         ri = l-1
        
#         while li<=ri:
#             i = (li+ri)//2
#             temprank = min(l-i,c[i])
#             print(li,ri,i,temprank,rank)
#             if rank and temprank <= rank:
#                 ri = i-1
#             else:
#                 li = i+1
#             rank = max(rank,temprank)
#         return max(rank,0)
        
        
        
        