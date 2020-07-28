from collections import deque

def getNeighbors(x,y,maze):
    n = len(maze)
    temp, neighbors = [[x,y+1], [x+1, y], [x,y-1], [x-1,y]], []
    for i,j in temp:
        if 0 <= i < n and 0 <= j < n and (maze[i][j] == 0 or (not removedWall and maze[i][j] == 1)):
            neighbors.append((i,j))


def dfs(x,y,maze,removedWall):
    # print(x,y,removedWall)
    if maze[x][y] == 1:
        if removedWall:
            return float('inf')
        else:
            removedWall = 1
    n, res = len(maze), float('inf')
    if (x,y) == (n-1,n-1):
        return 1
    
    
    ##Mark current cell visited
    maze[x][y] -= 2

    ##Get Neighbors
    temp, neighbors = [[x,y+1], [x+1, y], [x,y-1], [x-1,y]], []
    for i,j in temp:
        # print('Neighbors', i, j)
        if 0 <= i < n and 0 <= j < n and (maze[i][j] == 0 or (removedWall == 0 and maze[i][j] == 1)):
            neighbors.append((i,j))

    for i,j in neighbors:
        res = min(res,dfs(i,j,maze,removedWall)+1)

    ##Mark current cell as unvisited before leaving
    maze[x][y] += 2

    return res


def getChildrenAndGrandChildren(x,y,wallRemoved,maze):
    m,n = len(maze), len(maze[0])
    temp, temp2, children, grandchildren = [[x,y+1], [x+1, y], [x,y-1], [x-1,y]], [[x,y+2], [x+2, y], [x,y-2], [x-2,y]], set([]), set([])
    for k,p in enumerate(temp):
        i,j = p
        if 0 <= i < n and 0 <= j < n:# and (maze[i][j] == 0 or (not removedWall and maze[i][j] == 1)):
            children.add((i,j))
            if not wallRemoved and maze[i][j] == 1:
                gc_i, gc_j = temp2[k]
                if 0 <= gc_i < n and 0 <= gc_j < n:
                    grandchildren.add((gc_i,gc_j))
    return children, grandchildren

def getChildren(x,y,wallRemoved,m,n):
    # m,n = len(maze), len(maze[0])
    temp, children = [[x,y+1], [x+1, y], [x,y-1], [x-1,y]], set([])
    for i,j in temp:
        if 0 <= i < m and 0 <= j < n:# and (maze[i][j] == 0 or (not removedWall and maze[i][j] == 1)):
            children.add((i,j))
    return children

def solution(maze):
    m,n = len(maze), len(maze[0])
    Q, visited = deque([]), [[[0,0] for _ in row] for row in maze]
    #[x,y,nodecount,wallRemoved]
    Q.append((0,0,1,0))
    visited[0][0][0] = 1
    counter = 0
    while Q:# and counter < 30:
        counter += 1
        x,y,count,wallRemoved = Q.popleft()
        # print(x,y,wallRemoved)
        if (x,y) == (m-1,n-1):
            return count
        # visited[x][y] = 1
        children = getChildren(x,y,wallRemoved,m,n)
        
        # print('Next = ',end='')
        for c in children:
            xn,yn = c
            if (wallRemoved > 0 and maze[xn][yn] == 1) or visited[xn][yn][wallRemoved]:
                continue
            # print(c,end=', ')
            visited[xn][yn][wallRemoved + maze[xn][yn]] = 1
            Q.append((xn,yn,count+1, wallRemoved + maze[xn][yn]))
        # print('.')

def solution(maze):
    # lookup = [[ [0,0] for i in range(n)] for j in range(n)]
    #lookup[i][j][0] => lookup of i,j with not removedwall
    # return dfs(0,0,maze,0)
    return bfs(maze)


m = [[0,0,0],[0,1,0]]
print(solution(m))
m = [[0,1],[1,0]]
print(solution(m))
m = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(solution(m))
m = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(m))
m = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution(m))
maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(maze))