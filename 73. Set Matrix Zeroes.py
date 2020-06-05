class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        
        ##Mark Zeroes (top and left)
        i = 0
        origin = [1,1] #row,col
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    # print(i,j)
                    if j != 0 and i != 0:
                        matrix[0][j] = matrix[i][0] = 0
                    if j == 0:
                        origin[1] = 0
                    if i == 0:
                        origin[0] = 0
                j+=1
            i+=1

        ##Set Zeroes
        #Check columns first except first:
        c = 1
        while c < len(matrix[0]):
            if matrix[0][c] == 0:
                for i in range(len(matrix)):
                    matrix[i][c] = 0
            c+=1
        
        #Check Rows
        r = 1
        while r < len(matrix):
            if matrix[r][0] == 0:
                matrix[r] = [0]*len(matrix[0])
            r+=1
        
        #Check origin
        if origin[1] == 0:
            for c in range(len(matrix)):
                matrix[c][0] = 0
        if origin[0] == 0:
            matrix[0] = [0]*len(matrix[0])
            
        return