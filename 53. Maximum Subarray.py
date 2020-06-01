class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = nums[0]
        maxCount = count
        for i in range(1,len(nums)):
            count = max(count,0)+nums[i]
            maxCount = max(maxCount,count)
            
        return maxCount