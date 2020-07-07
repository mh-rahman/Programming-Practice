class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def getRow(matrix,target):
            start,end = 0, len(matrix)-1
            while start <= end:
                mid = (start+end)//2
                if target > matrix[mid][-1]:
                    start = mid+1
                elif target < matrix[mid][0]: 
                    end = mid-1
                else:
                    start = mid
                    break
            return start
        
        
        def search(matrix,row,target):
            print("Searching in row:",row)
            start,end,res = 0, len(matrix[row])-1,target == matrix[row][0]
            while start <= end:
                mid = (start+end)//2
                if target > matrix[row][mid]:
                    res = False
                    start = mid+1
                elif target < matrix[row][mid]:
                    res = False
                    end = mid-1
                else:
                    res = True
                    break
            return res
            
            
            
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row = getRow(matrix,target)
        return search(matrix,row,target)
        