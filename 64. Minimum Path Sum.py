class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        
        for j in range(1,col):
            grid[0][j]+=grid[0][j-1]
        
        for i in range(1,row): 
            grid[i][0]+=grid[i-1][0]
            
        for i in range(1,row):
            for j in range(1,col):
                grid[i][j]+=min(grid[i-1][j], grid[i][j-1])
            
        # print(grid,row,col)
        
        return grid[-1][-1] # if col != 0 else 0