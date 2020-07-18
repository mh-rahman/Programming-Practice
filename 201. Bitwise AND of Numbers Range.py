class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

    def myRangeBitwiseAnd(self, m: int, n: int) -> int:
        res1, temp1, temp2 = m & n, m+1, n-1
        while res1 and temp1 <= temp2:
            res1 = res1 & temp1
            res1 = res1 & temp2
            temp1 += 1
            temp2 -= 1
        return res1
        