class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #construct trie?
        #START -> start chars -> middle chars -> leafs = END
        
        def getTrie(words):
            root = node('START')
            for word in words:
                curr = root
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = node(c)
                    curr = curr.children[c]
                curr.children['END'] = node('END')
            return root
        
        def printTrie(root):
            Q = deque()
            Q.append(('',root,1))
            while Q:
                parent,curr,level = Q.popleft()
                print(parent,curr.val,level)
                for c in curr.children:
                    Q.append((curr.val,curr.children[c],level+1))
            return
        
        def getCell(i,j,board):
            if 0<=i<len(board) and 0<=j<len(board[0]):
                return [i,j]
            else:
                return None
            
        
        def helper(pos,curr,constructed):
            # print(pos,curr.val,constructed)
            if 'END' in curr.children:
                res.add(''.join(constructed))
            i,j = pos
            neighbours = []
            neighbours.append(getCell(i-1,j,board))
            neighbours.append(getCell(i+1,j,board))
            neighbours.append(getCell(i,j-1,board))
            neighbours.append(getCell(i,j+1,board))
            for n in neighbours:
                if n is None:
                    continue
                x,y = n
                c = board[x][y]
                if c in curr.children:
                    constructed.append(c)
                    board[x][y] = ""
                    helper(n,curr.children[c],constructed)
                    constructed.pop()
                    board[x][y] = c
        
        
        
        if not words or not board:
            return []
        root = getTrie(words)
        # printTrie(root)
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c in root.children:
                    board[i][j] = ""
                    # print('Starting with',c)
                    helper([i,j],root.children[c],[c])
                    board[i][j] = c
                
        print(res)
        
        return res
        

class node:
    def __init__(self,val):
        self.val = val
        # self.children = [] 
        self.children = {} # char to node mapping
        
    