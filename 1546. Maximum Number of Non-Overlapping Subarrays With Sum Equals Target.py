
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        
        def helper1(ind, currCount):
            # print(ind, currCount)
            if ind == len(nums):
                self.count = max(self.count, currCount)
                return 
            s = 0
            for i in range(ind, len(nums)):
                s += nums[i]
                if s == target:
                    # print('Subarray',ind,i)
                    helper(i+1, currCount+1)
            helper(ind+1, currCount)
            return
        
        def helper(nums,ind):
            if ind in self.lookup:
                return self.lookup[ind]
            s, count = 0, 0
            for i in range(ind, len(nums)):
                s += nums[i]
                if s == target:
                    # print('Subarray',ind,i)
                    count = max(count, 1+helper(nums, i+1))
            count = max(count, helper(nums, ind+1))
            self.lookup[ind] = count
            return count

        self.lookup = {len(nums): 0}
        # print(self.lookup)
        return helper(nums,0)
        # return self.count