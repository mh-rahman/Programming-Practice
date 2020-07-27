class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0,1 -> 3,0
        n, i = len(matrix), 0
        while i < n//2:
            # print('Level =',i)
            for j in range(i,n-i-1):
                # print(matrix[i][j], matrix[j][-i-1],matrix[-i-1][-j-1],matrix[-j-1][i])
                matrix[i][j], matrix[j][-i-1],matrix[-i-1][-j-1],matrix[-j-1][i] = matrix[-j-1][i], matrix[i][j], matrix[j][-i-1],matrix[-i-1][-j-1]
            i += 1
        return 
