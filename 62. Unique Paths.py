class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def getNeighbors(i,j):
            temp = []
            if j+1 < len(res[0]):
                temp.append([i,j+1])
            if i+1 < len(res):
                temp.append([i+1,j])
            
            return temp
            
        res = [[0]*m for _ in range(n)]
        res[-1][-1] = 1
        s = m+n-2-1
        while s>=0:
            i = min(n-1,s)
            j = s-i
            while j<m and i>=0:
                count = 0
                neighbors = getNeighbors(i,j)
                for neighbor in neighbors:
                    count+=res[neighbor[0]][neighbor[1]]
                    
                res[i][j] = count
                j+=1
                i-=1
            s-=1
        return res[0][0]