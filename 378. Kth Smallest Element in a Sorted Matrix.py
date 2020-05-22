import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if k==1:
            return matrix[0][0]
        
        if k==n*n:
            return matrix[n-1][n-1]
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap,matrix[i][j])
                
        res = matrix[0][0]
        while k>0:
            res = heapq.heappop(heap)
            k-=1
            
        # print(res)
        
        return res