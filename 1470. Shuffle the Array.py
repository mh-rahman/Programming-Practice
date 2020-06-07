class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l = len(nums)//2
        for i in range(l):
            res.append(nums[i])
            res.append(nums[i+l])
            
        return res