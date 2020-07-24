class Solution:
    def reverse(self, x: int) -> int:
        s, res, lim = 1, 0, 2**31
        if x < 0:
            if x == -lim:
                return 0
            s = -1
            x = abs(x)
        while x > 0:
            res = res*10 + x%10
            x = x//10
        if res > lim -1 or res < -lim:
            return 0
        return s*res