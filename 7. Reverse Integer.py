class Solution:
    def reverse(self, x: int) -> int:
        x = -1*int(''.join(reversed(list(str(abs(x)))))) if x<0 else int(''.join(reversed(list(str(abs(x))))))
        if x < -1*2**31 or x >= 2**31:
            return 0
        return x