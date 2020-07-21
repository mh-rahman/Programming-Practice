# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        st, end = 0, n
        while st <= end:
            mid = (st + end)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                st = mid + 1
            else:
                end = mid - 1
