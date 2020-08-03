class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_lookup = {0:-1} #count: init_index
        count, res = 0, 0
        
        for i,n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
            if count in count_lookup:
                res = max(res, i-count_lookup[count])
            else:
                count_lookup[count] = i
        return res