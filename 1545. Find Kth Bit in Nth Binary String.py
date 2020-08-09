class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        i = 1
        s = [0]
        while i < n:
            i += 1
            s = s + [1] + [1 if x == 0 else 0 for x in s[::-1]]
        return str(s[k-1])