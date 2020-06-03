class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        res = [0]*(n+1)
        res[-1] = 1
        res[-2] = 1
        for i in range(n-2,-1,-1):
            res[i] = res[i+1]+res[i+2]
            # print(i,res)
        
        return res[0]
            