class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        M = len(board)
        
        if M == 0:
            return []
        
        N = len(board[0])
        
        def getN(i,j):
            temp = []
            temp.append((max(0,i-1),j))
            temp.append((min(M-1,i+1),j))
            temp.append((i,max(0,j-1)))
            temp.append((i,min(N-1,j+1)))
            try:
                temp.remove((i,j))
            except:
                pass
            return [(x,y) for (x,y) in set(temp) if board[x][y] == 'O']
        
        def markSafe(i,j):
            board[i][j] = 'S'
            neighbors = getN(i,j)
            for (x,y) in neighbors:
                markSafe(x,y)
                
            return
        
        for i in [0,M-1]:
            for j in range(N):
                if board[i][j] == 'O':
                    markSafe(i,j)
                    
                    
        for j in [0,N-1]:
            for i in range(M):
                if board[i][j] == 'O':
                    markSafe(i,j)
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        return board
            