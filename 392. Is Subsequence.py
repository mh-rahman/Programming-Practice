class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        idx = 0
        l = len(s)
        for c in t:
            if c == s[idx]:
                idx+=1
            if idx == l:
                break
        
        if idx == l:
            return True
        else:
            return False