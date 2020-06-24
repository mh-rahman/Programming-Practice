class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*n
        
        def helper(st,end):
            # print(st,end)
            if end < st+1:
                return 1
            if dp[end-st]:
                return dp[end-st]
            res = 0
            for i in range(st,end+1):
                res+=(helper(st,i-1)*helper(i+1,end))
                
            dp [end-st] = res
            return res
        
        n = helper(1,n)
        # print(n)
        # print(dp)
        return n
        