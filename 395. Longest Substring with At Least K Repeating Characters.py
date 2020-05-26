class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
#         def doesSatisfy():
#             # flag = True
#             for val in chardict.values():
#                 if val != 0 and val != k:
#                     return False
#             return True
        
#         start = 0
#         end = 0
#         maxlen = 0
#         chardict = {chr(c):0 for c in range(ord('a'),ord('z')+1)}
        
#         while end<k:
#             chardict[s[end]]+=1
#             end+=1
#         # print(chardict.values())
#         if doesSatisfy():
#             maxlen = k
#         while start + maxlen < len(s):
#             while end<len(s):
#                 end+=1
#             start+=1
        
        def doesSatisfy(vals):
            # flag = True
            for val in vals:
                if val != 0 and val < k:
                    return False
            return True
        
        def condCheck2(values):
            flag = True
            for val in values:
                if val >= k:
                    flag = False
                    break
            return flag
        
        if not s:
            return 0
        if k == 1:
            return len(s)
        
        flag = False
        temp = collections.Counter(s)
        for val in temp.values():
            if val >= k:
                flag = True
                break
        
        if not flag:
            return 0
        
        
        maxlen = 0
        res = [[None]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            res[i][i] = collections.Counter(s[i])
            

        # ##Iterative bottom-up
        # window = 1
        # while window < len(s):
        #     idx = 0
        #     while idx + window < len(s):
        #         res[idx][idx+window] = res[idx][idx+window-1]+res[idx+window][idx+window]
        #         if doesSatisfy(res[idx][idx+window].values()):
        #             maxlen = max(maxlen,window+1)
        #         idx+=1
        #     window+=1

        for i in range(len(s)):
            res[i][len(s)-1] = collections.Counter(s[i:len(s)])
        
        idx = 0
        condCheck2_flag = False
        while idx < len(s):
            end = len(s) - 1
            while end - idx >= 0:
                if end+1 < len(s):
                    res[idx][end] = res[idx][end+1] - res[end+1][end+1]
                if doesSatisfy(res[idx][end].values()):
                    maxlen = max(maxlen,end-idx+1)
                    # return maxlen
                elif condCheck2(res[idx][end].values()):
                    # print(idx,end,res[idx][end].values())
                    condCheck2_flag = True
                    break
                end-=1
            idx+=1
        
        # print(res)
        
        return maxlen

    
    
    
    
    
    
    
    
    
    
    
    
    
            
        