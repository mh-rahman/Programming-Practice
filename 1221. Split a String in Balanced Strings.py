class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        for c in s:
            if c == 'R':
                count += 1
            elif c == 'L':
                count -= 1
            if count == 0:
                res += 1
        return res
                
        