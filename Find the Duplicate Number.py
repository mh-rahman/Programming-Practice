class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if l < 3: return nums[0]
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return nums[i]