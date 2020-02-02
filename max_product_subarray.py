class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_max = temp_min = temp_max = nums[0]
        for x in nums[1:]:
            if x < 0:
                temp_min, temp_max = temp_max, temp_min
            temp_min = min(x,temp_min*x)
            temp_max = max(x,temp_max*x)
            
            final_max = max(final_max, temp_max)
            
        return final_max