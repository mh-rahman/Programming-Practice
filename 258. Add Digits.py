class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        return 1 + (num-1)%9