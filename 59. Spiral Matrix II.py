class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a, res = 1, [[0]*n for _ in range(n)]
        for k in range(n//2 + 1):
            # starting = (k,k)
            # print(k,n-k-1)
            
            if k == n-k-1:
                res[k][k] = a
                break
            
            # Top row
            for j in range(k, n-k-1):
                res[k][j] = a
                a += 1
            
            # Right col
            for i in range(k, n-k-1):
                res[i][n-k-1] = a
                a += 1
            
            # Bottom row:
            for j in range(n-k-1, k, -1):
                res[n-k-1][j] = a
                a += 1
                
            # Left Col
            for i in range(n-k-1, k, -1):
                res[i][k] = a
                a += 1
                
            # print(res)
        
        return res