class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # print(set([(1,2), (1,2)] ))
        def getN(i,j):
            res = set([])
            res.add((max(0,i-1),j))
            res.add((i,max(0,j-1)))
            res.add((i,min(len(matrix[0])-1,j+1)))
            res.add( (min(len(matrix)-1,i+1),j))
            
            temp = []
            
            for (x,y) in res:
                if matrix[x][y] > matrix[i][j]:
                    temp.append((x,y))
            
            return temp
        
        def count(ij):
            i,j = ij
            neighbors = getN(i,j)
            # global path_matrix
            if path_matrix[i][j] == -1:
                temp = 1
                for neighbor in neighbors:
                    temp = max(temp, count(neighbor)+1)
                path_matrix[i][j] = temp
                return temp
            else:
                return path_matrix[i][j]
        
        
        # print(getN(1,1) )
        
        path_matrix = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        
        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if path[i][j] != -1:
                max_path = max(max_path, count((i,j)))
        
        # print(path_matrix)
        
            
        return max_path