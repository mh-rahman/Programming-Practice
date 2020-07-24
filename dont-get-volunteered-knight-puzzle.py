import collections

def getNeighbors(x,y):
    res = set([])
    for i in range(max(0,x-2),min(7,x+2)+1):
        if i == x:
            continue
        for j in range(max(0,y-2),min(7,y+2)+1):
            if j == y:
                continue
            if abs(x-i) + abs(y-j) == 3:
                res.add((i,j))
    return res



def solution(src,dst):
    '''
    1. Maintain a set of next possible squares i.e. nextCells
    (Set instead of list since one cell can be reached in multiple ways, atleast two, in a single move)
    **Use tuples to store values - 8 possible values
    2. Add them to a queue (BFS)
    3. Mark current square before moving to next (to avoid revisiting)
    4. If a cell is visited, dont add it to 'nextCells' set
    5. If dst is found, return the depth or 'moves' value
    '''
    if src == dst:
        return 0
    si, sj = src//8, src%8
    di, dj = dst//8, dst%8
    board = [[0 for i in range(8)] for j in range(8)]
    Q = collections.deque([])
    Q.append((si,sj,0))
    while Q:
        curri, currj, moves = Q.popleft()
        board[curri][currj] = 1
        neighbors = getNeighbors(curri,currj)
        for xn,yn in neighbors:
            if (xn,yn) == (di,dj):
                return moves+1
            if board[xn][yn] == 0:
                Q.append((xn,yn, moves+1))

# print(solution(0,1))
# print(solution(19,36))
# print(solution(62,0))

