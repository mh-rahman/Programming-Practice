class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        def dfs(x,y,A,lookup):
            # print('At', x,y)
            if x == len(A)-1:
                # print('Path sum at ({},{}):'.format(x,y), A[x][y])
                return A[x][y]
            if (x,y) in lookup:
                # print('Lookup!')
                return lookup[(x,y)]
            pathSum = math.inf
            for j in range(max(0, y-1), min(len(A[0]), y+2)):
                pathSum = min(pathSum, dfs(x+1,j,A,lookup))
            pathSum += A[x][y]
            # print('Path sum at ({},{}):'.format(x,y), pathSum)
            lookup[(x,y)] = pathSum
            return pathSum
        
        if not A:
            return 0
        res, lookup = math.inf, {}
        for i in range(len(A[0])):
            res = min(res, dfs(0,i,A,lookup))
        return res