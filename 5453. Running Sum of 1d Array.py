class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        idx = 0
        while idx < len(nums):
            nums[idx]+=prev
            prev = nums[idx]
            idx+=1
        return nums