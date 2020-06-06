class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def getN(i,j,c):
            res = []
            for x in range(max(0,i-1),min(i+1,len(board[0])-1)+1):
                for y in range(max(0,j-1),min(j+1,len(board)-1)+1):
                    # print(x,y,board[x][y])
                    if x == i and y == j:
                        continue
                    if (x == i or y == j) and board[x][y] == c:
                        res.append([x,y])
            return res
        
        def getValidN(N,c):
            res = []
            for x,y in N:
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == c and not visited[x][y]:
                    res.append([x,y])
            return res
        
        def helper(pos,word):
            if not word:
                return True
            i,j = pos
            visited[i][j] = 1
            temp = [[i-1,j],[i,j+1],[i+1,j],[i,j-1] ]
            neighbors = getValidN(temp,word[0])
            for n in neighbors:
                if helper(n,word[1:]):
                    return True
            visited[i][j] = 0
            return False

        
        i = j = 0
        visited = [[0 for __ in _] for _ in board]
        for i,row in enumerate(board):
             for j,c in enumerate(board[i]):
                    if c != word[0]:
                        continue
                    elif helper([i,j],word[1:]):
                        return True
        
        return False
                    