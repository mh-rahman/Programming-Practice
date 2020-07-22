class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        lookup, min_len = {}, len(nums) #num: [count, low, high]
        for i in range(len(nums)):
            n = nums[i]
            if n not in lookup:
                lookup[n] = [0,i,i]
            lookup[n][0] += 1
            lookup[n][2] = i
        x = max(lookup, key = lambda x: (lookup[x][0],lookup[x][1]-lookup[x][2]))
        return lookup[x][2]-lookup[x][1] + 1