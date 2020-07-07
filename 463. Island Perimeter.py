class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def getN(grid,x,y):
            n = []
            i = max(0,x-1)
            if x > 0 and grid[x-1][y] != 0:
                n.append([x-1,y])
            if x < len(grid)-1 and grid[x+1][y] != 0:
                n.append([x+1,y])
            if y > 0 and grid[x][y-1] != 0:
                n.append([x,y-1])
            if y < len(grid[0])-1 and grid[x][y+1] != 0:
                n.append([x,y+1])
            return n

                
        if not grid or not grid[0]:
            return 0
        flag,x,y = False,0,0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 1:
                    x,y = i,j
                    flag = True
                    break
            if flag:
                break
        
        
        
        if not flag:
            return 0
        
        Q, perimeter = deque([[x,y]]), 0
        grid[x][y]*=-1
        
        while Q:
            x,y = Q.popleft()
            neighbors = getN(grid,x,y)
            perimeter+=(4 - len(neighbors))
            for n in neighbors:
                x1,y1 = n
                if grid[x1][y1] > 0:
                    grid[x1][y1] = -1
                    Q.append(n)
        
        return perimeter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        