class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def helper(s,idx,wordDict) -> None:
            if lookup[idx] != None:
                return lookup[idx]
            if idx >= len(s):
                return ['']
            curr = ''
            res = []
            i = idx
            while idx < len(s):
                c = s[idx]
                curr+=c
                if curr in wordDict:
                    if idx+1 < len(s):
                        res+=[(curr + ' ' + x) for x in helper(s,idx+1,wordDict)]
                    else:
                        res.append(curr)
                    
                idx+=1
            lookup[i] = res
            return res
            
        
        lookup = {i:None for i in range(len(s))}
        res = helper(s,0,wordDict)
        return res