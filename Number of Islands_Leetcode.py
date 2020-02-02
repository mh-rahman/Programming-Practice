class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def makeZero(grid, i, j):
            if i < 0 or i > len(grid): return
            if j < 0 or j > len(grid[0]): return
            grid[i][j] = 0
            if int(grid[max(0,i-1)][j]) == 1:
                makeZero(grid, max(0,i-1), j)
            if int(grid[i][max(0,j-1)]) == 1:
                makeZero(grid, i, max(0,j-1))
            if int(grid[min(rows-1,i+1)][j]) == 1:
                makeZero(grid, min(rows-1,i+1), j)
            if int(grid[i][min(cols-1,j+1)]) == 1:
                makeZero(grid, i, min(cols-1,j+1))
        
        if len(grid) == 0: return 0
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if int(grid[i][j]) == 1:
                    count+=1
                    makeZero(grid,i,j)
                    # if int(grid[i][j]) == 1 and grid[min(rows-1,i+1)][j] != -1 and grid[i][min(cols-1,j+1)] != -1:
                    #     count+=1
                    #     grid[i][j] = -1
                    # if int(grid[min(rows-1,i+1)][j]) == 1: grid[min(rows-1,i+1)][j] = -1 
                    # if int(grid[i][min(cols-1,j+1)]) == 1: grid[i][min(cols-1,j+1)] = -1 
        return count