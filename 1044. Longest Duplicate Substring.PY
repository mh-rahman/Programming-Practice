class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) //2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
        
        
        while False:
        ## Linear Window search 
        # res,maxLenght,l,lookup,win = '',0,len(s),{},1
        # newDict = {c:[] for c in S}
        # for i,c in enumerate(S):
        #     newDict[c].append(i)
        # while newDict:
        #     del(lookup)
        #     lookup, newDict = newDict, {}
        #     for s in lookup:
        #         if len(lookup[s]) < 2:
        #             continue
        #         res = s
        #         for i in lookup[s]:
        #             if i+win >= l:
        #                 break
        #             temp = s + S[i+win]
        #             if temp in newDict:
        #                 newDict[temp].append(i)
        #             else:
        #                 newDict[temp] = [i]
        #     win+=1
        # return res
            pass
        
        while False:
            #### Binary Window Search (Better)
#             res = ''
#             l = len(S)
#             newDict = {c:[] for c in S}
#             for i,c in enumerate(S):
#                 newDict[c].append(i)
#             if len(newDict) == 1:
#                 return S[0]*(l-1)
#             lookup = {}

#             startw,win,endw,flag = 0,0,l-1,True
#             while startw < endw: #To Be Modified
#                 if flag:
#                     del(lookup)
#                     startw, lookup = win+1, newDict
#                 else:
#                     endw = win-1
#                 win,newDict,flag = {},False,(startw+endw)//2
#                 for s in lookup:
#                     if len(lookup[s]) < 2:
#                         continue
#                     for i in lookup[s]:
#                         if i+win >= l:
#                             break
#                         temp = s+S[i+len(s):i+win+1]
#                         if temp in newDict:
#                             res,flag = temp,True
#                             newDict[temp].append(i)
#                         else:
#                             newDict[temp] = [i]
#             return res
            pass

        while False:
            ## Naive approach
#             for idx in range(l):
#                 if idx >= l - maxLength:
#                     break
#                 for i in range(idx+1):
#                     if idx+1-i <= maxLength:
#                         break
#                     temp = S[i:idx+1]
#                     # print(idx,i,temp)
#                     if temp in lookup:
#                         if len(temp) > maxLength:
#                             maxLength = len(temp)
#                             res = temp
#                     else:
#                         lookup.add(temp)

#             return 'ana' if S == 'banana' else ''
            pass

        return res