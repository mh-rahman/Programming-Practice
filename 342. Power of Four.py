class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return 2 ** 32 % num == 0 and int(num ** 0.5) ** 2 == num