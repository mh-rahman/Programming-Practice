class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [x for x,y in Counter(nums).items() if y == 1][0]