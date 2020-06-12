class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(l,r):
            if r<=l:
                return l
            m = (l+r)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            if nums[m-1] > nums[m]:
                return helper(l,m-1)
            return helper(m+1,r)

        
        if len(nums) < 2 or nums[0] > nums[1]:
            return 0
        return helper(1,len(nums)-1)