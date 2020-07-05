class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        # print(nums)
        max_length = length = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                length+=1
                max_length = max(max_length,length)
            else:
                length = 1
                
        return max_length