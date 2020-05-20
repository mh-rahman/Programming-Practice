class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getVal(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return 0
            else:
                return abs(board[i][j])
            
        def getNeighbors(x,y):
            neighbors = []
            i = x-1
            while i<x+2:
                j = y-1
                while j<y+2:
                    if i == x and j == y:
                        j+=1
                        neighbors.append(0)
                        continue
                    else:
                        neighbors.append(getVal(i,j))
                    j+=1
                i+=1
            # print(x,y,neighbors)
            return neighbors
        
        ##Firstly, increase all values by 1, i.e mapping 0:1 and 1:2
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                board[i][j]+=1
                
        ##Update the values: -ve implies the value must be updated
        for i in range(m):
            for j in range(n):
                neighbors = getNeighbors(i,j)
                if board[i][j] == 1: ##Dead cell:
                    if neighbors.count(2) == 3:
                        board[i][j] = -1
                else:
                    if neighbors.count(2) < 2 or neighbors.count(2) > 3:
                        board[i][j] = -2
                
        
        ##Before returning, reduce all values by 1, i.e. reverse mapping
        
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j]-=1
                else:
                    if board[i][j] == -1:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                        
        return board
                    
                
                        
        
        
        
        
        
        
        
        
        
        
        