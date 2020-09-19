class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        distinct = {}
        start = curr = 0
        res = 0
        while curr < len(s):
            c = s[curr]
            if c not in distinct:
                distinct[c] = 0
            distinct[c] += 1
            while len(distinct) > k:
                sc = s[start]
                distinct[sc] -= 1
                if distinct[sc] <= 0:
                    del(distinct[sc])
                start += 1
            res = max(res, curr-start+1)
            curr += 1
        return res
                