class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def knapSack(W, wt, val):
            n = len(wt)
            K = [[0 for x in range(W+1)] for x in range(n+1)] 
            # Build table K[][] in bottom up manner 
            for i in range(n+1): 
                for w in range(W+1): 
                    if i==0 or w==0: 
                        K[i][w] = 0
                    elif wt[i-1] <= w: 
                        K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
                    else: 
                        K[i][w] = K[i-1][w] 

            return K[n][W]
        
        total = sum(nums)
        
        if len(nums) < 2 or total%2 == 1:
            return False
        
        if knapSack(total//2,nums,nums) == total//2:
            return True           
        
        return False