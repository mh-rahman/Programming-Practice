class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        return (m1-1)*(m2-1)