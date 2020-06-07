class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        swaps = orig = idx = 0
        temp = nums[idx]
        while k and swaps < l:
            sw = (idx+k)%l
            nums[sw], temp = temp, nums[sw]
            swaps+=1
            idx = sw
            if idx == orig and swaps<l:
                idx+=1
                orig = idx
                temp = nums[idx]
        return 
