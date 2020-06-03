class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(nums):
            nums = collections.Counter(nums)
            for n in nums.keys():
                if n == '.':
                    continue
                elif nums[n] > 1:
                    return False
                else:
                    continue
            return True 
        

        for row in board:
            if not isValid(row):
                return False

        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not isValid(col):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                sqr = board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                if not isValid(sqr):
                    return False
                
        return True
        
        