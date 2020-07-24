class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        opt__ = nums[0]
        opt_ = max(nums[0],nums[1])
        for num in nums[2:]:
            opt = max(opt__+num, opt_)
            opt__ = opt_
            opt_ = opt
            
        return opt