class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        l = len(s)
        for i,c in enumerate(s):
            res = res + (ord(c)-ord('A')+1)*(26**(l-i-1))
        return res