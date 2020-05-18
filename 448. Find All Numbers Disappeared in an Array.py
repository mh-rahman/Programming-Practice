class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -1*abs(nums[abs(nums[i])-1])
            # print(i,nums[i],nums)
        res = []
        for i,x in enumerate(nums):
            if x>0:
                res.append(i+1)
                
        return res
        