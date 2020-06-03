class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # req = 0
        # for n in nums[:0:-1]:
        #     if n < req:
        #         req+=1
        #     else:
        #         req = 1
        # if nums[0] < req:
        #     return False
        # return True
        
        i = 1
        safe = nums[0]
        while i<len(nums):
            if not safe:
                return False
            n = nums[i]
            if n:
                safe = max(n,safe-1)
            else:
                safe-=1
            i+=1
        
        return True
            