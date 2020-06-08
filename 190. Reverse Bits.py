class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 32
        while count:
            res = res<<1
            x = n&1
            res+=x
            n = n>>1
            # print(n,res,x)
            count-=1
        return res