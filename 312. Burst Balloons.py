class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def getNum(i):
            if i<0 or i>=len(nums):
                return 1
            else:
                return nums[i]
            
        def getOpt(i,j):
            if i<0 or i>=len(nums) or j<0 or j>=len(nums) :
                return 0
            else:
                return opt[i][j]
        
        n = len(nums)
        if n == 0:
            return 0
        # n = len(nums) - 1
        opt = [[0]*(n) for i in range(n)]
        
        for i in range(n):
            opt[i][i] = getNum(i-1)*getNum(i)*getNum(i+1)
            
        for i in range(1,n):
            for x in range(n):
                y = x+i
                if y>=n:
                    break
                else:
                    temp = 0
                    for j in range(x,y+1):
                        temp2 = getNum(x-1)*getNum(j)*getNum(y+1) + getOpt(x,j-1) + getOpt(j+1,y)
                        temp = max(temp, temp2)
                    
                    
                    opt[x][y] = temp
                    
        # print(opt)
        return opt[0][-1]
                

                
                
                
                
                
                
                
                
                
                