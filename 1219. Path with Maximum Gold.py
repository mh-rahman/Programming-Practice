class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x,y,grid):
            
            grid[x][y] *= -1
            gold = 0
            neighbors = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
            for n in neighbors:
                i,j = n
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0:
                    temp = dfs(i,j,grid)
                    gold = max(gold,temp)
            
            grid[x][y] *= -1
            gold += grid[x][y]
            # print('Gold collected at ({},{}) = {}'.format(x,y,gold))
            return gold
        
        
        goldenCells = [(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] > 0]
        maxGold = 0
        for x,y in goldenCells:
            temp = dfs(x,y,grid)
            # print('start = ({},{}), Gold = {}'.format(x,y,temp))
            maxGold = max(maxGold, temp)
        return maxGold