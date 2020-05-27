class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            # if n == 0:
            #     return 1
            # if n == 1:
            #     return x
            if helperDict.get(n,-1) == -1:
                res = helper(x,n//2)*helper(x,n-n//2)
                helperDict[n] = res
            res = helperDict[n]
            return res
        
        if x == 1:
            return 1
        if x == -1:
            return 1 if n%2 == 0 else -1
        
        helperDict = {0:1,1:x}
        if n < 0:
            return 1/helper(x,abs(n))
        return helper(x,n)
        