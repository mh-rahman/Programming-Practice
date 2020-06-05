class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[n] for n in nums]
        while res and len(res[0]) < len(nums):
            res = [s+[c]  for s in res for c in nums if c not in s]
        return res
        
        