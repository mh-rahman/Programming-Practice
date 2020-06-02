class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l
        
        idx = 0
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                nums[idx] = nums[i]
                idx+=1
            
        nums[idx] = nums[-1]
        return idx+1
            