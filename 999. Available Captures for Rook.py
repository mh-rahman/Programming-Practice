class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def getRookPos(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return i,j            
        br,bc = getRookPos(board)
        pawns = 0
        
        c = bc-1
        while c >= 0:
            if board[br][c] == '.':
                c -= 1
                continue
            elif board[br][c] == 'p':
                pawns += 1
                break
            else:
                break
                
        c = bc+1
        while c < 8:
            if board[br][c] == '.':
                c += 1
                continue
            elif board[br][c] == 'p':
                pawns += 1
                break
            else:
                break
                
        r = br-1
        while r >= 0:
            if board[r][bc] == '.':
                r -= 1
                continue
            elif board[r][bc] == 'p':
                pawns += 1
                break
            else:
                break
                
        r = br+1
        while r < 8:
            if board[r][bc] == '.':
                r += 1
                continue
            elif board[r][bc] == 'p':
                pawns += 1
                break
            else:
                break
        
        return pawns