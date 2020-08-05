class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # consider water flowing reverse: always flows from smaller to bigger number
        # Initializ a zero matrix - top row and left col will be 1 (pacific) and bottom row and right col will be 2 (atlantic)
        # Separately process for pacific (1) and atlantic (2)
        
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        # flow, res = self.initialize(m,n), []
        flow, res = [[0 for _ in range(n)] for row in range(m)], []

        # pacific - top row (flow = 1)
        for i in range(n):
            if flow[0][i] in [1,3]:
                continue
            Q = deque([])
            Q.append((0,i))
            flow[0][i] += 1
            while Q:
                x,y = Q.popleft()
                for i,j in [(x+1, y),(x-1, y),(x, y-1),(x, y+1)]:
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] >= matrix[x][y] and flow[i][j] in [0,2]:
                        flow[i][j] += 1
                        Q.append((i,j))
                        
        # pacific - left col (flow = 1)
        for i in range(1,m):
            if flow[i][0] in [1,3]:
                continue
            Q = deque([])
            Q.append((i,0))
            flow[i][0] += 1
            while Q:
                x,y = Q.popleft()
                for i,j in [(x+1, y),(x-1, y),(x, y-1),(x, y+1)]:
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] >= matrix[x][y] and flow[i][j] in [0,2]:
                        flow[i][j] += 1
                        Q.append((i,j))

        
        # Atlantic - Bottom row (flow = 2)
        for i in range(n):
            if flow[m-1][i] in [2,3]:
                continue
            Q = deque([])
            Q.append((m-1,i))
            flow[m-1][i] += 2
            while Q:
                x,y = Q.popleft()
                for i,j in [(x+1, y),(x-1, y),(x, y-1),(x, y+1)]:
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] >= matrix[x][y] and flow[i][j] in [0,1]:
                        flow[i][j] += 2
                        Q.append((i,j))
        
        
        # Atlantic - Right col (flow = 2)
        for i in range(m-1):
            if flow[i][n-1] in [2,3]:
                continue
            Q = deque([])
            Q.append((i,n-1))
            flow[i][n-1] += 2
            while Q:
                x,y = Q.popleft()
                for i,j in [(x+1, y),(x-1, y),(x, y-1),(x, y+1)]:
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] >= matrix[x][y] and flow[i][j] in [0,1]:
                        flow[i][j] += 2
                        Q.append((i,j))

        # self.printFlow(flow)
        
                
        for i in range(m):
            for j in range(n):
                if flow[i][j] == 3:
                    res.append([i,j])
        
        return res
    
    def initialize(self,m,n):
        flow = [[0 for _ in range(n)] for row in range(m)]
        
        # pacific - top row
        for i in range(n):
            flow[0][i] += 1
        
        # pacific - left col (except first)
        for i in range(1,m):
            flow[i][0] += 1
            
        # atlantic - bottom row
        for i in range(n):
            flow[-1][i] += 2
        
        # atlantic - right col (except the last)
        for i in range(m-1):
            flow[i][-1] += 2
            
        return flow
    
    def printFlow(self, flow):
        print('######################')
        for row in flow:
            print(row)
        print('######################')
        return