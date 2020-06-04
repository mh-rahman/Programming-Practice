class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        l = len(nums)
        if not nums:
            return 1
        
        while i < l:
            if nums[i] == None:
                i+=1
                continue
            if nums[i] == i+1:
                nums[i] = None
                i+=1
                continue
            if 0<nums[i]<=l:
                idx = nums[i]-1
                if nums[idx] == None:
                    i+=1
                    continue
                nums[i] = nums[idx]
                nums[idx] = None
            else:
                i+=1

        for i,n in enumerate(nums):
            if n != None:
                return i+1
        
        return l+1