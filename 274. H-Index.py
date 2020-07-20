class Solution:
    def hIndex(self, c: List[int]) -> int:
        i,max_ct = 0,0
        c.sort(reverse = True)
        while i < len(c):
            n = c[i]
            ct = min(i+1,n)
            max_ct = max(ct,max_ct)
            i += 1
        return max_ct