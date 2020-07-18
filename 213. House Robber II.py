class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums,start,end):
            res = [0]*(end-start+1)
            res[0],res[1] = nums[start], max(nums[start],nums[start+1])
            i = 2
            while i+start <= end:
                res[i] = max(nums[i+start]+res[i-2],res[i-1])
                i += 1
            return res[-1]
                
        if len(nums) < 4:
            return max(nums) if nums else 0
        return max(helper(nums,0,len(nums)-2), helper(nums,1,len(nums)-1))