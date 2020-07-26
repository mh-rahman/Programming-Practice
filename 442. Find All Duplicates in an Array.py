class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        for i in range(n):
            ind = nums[i]%(n+1) - 1
            nums[ind] += (n+1)
        
        for i in range(n):
            if nums[i]//(n+1) == 2:
                res.append(i+1)
                
        return res