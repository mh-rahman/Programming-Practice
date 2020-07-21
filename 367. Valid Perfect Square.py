class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num in [0,1]:
            return True
        i = 1
        while i <= num//2 and i*i <= num:
            if i*i == num:
                return True
            i += 1
        return False