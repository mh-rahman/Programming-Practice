class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) <= 0:
            self.matrix = None
            return
        r,c = len(matrix), len(matrix[0])
        # smatrix = [[0]*c for i in range(r)]
        
        for i in range(1,c):
            matrix[0][i] += matrix[0][i-1]
        for i in range(1,r):
            matrix[i][0] += matrix[i-1][0]
            
        for i in range(1,r):
            for j in range(1,c):
                matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])
        self.matrix = [[matrix[i][j] for j in range(c)] for i in range(r)]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.matrix:
            return
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)