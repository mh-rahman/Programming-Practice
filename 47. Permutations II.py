class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums):
            res = []
            if not nums:
                return [[]]
            for i in set(nums):
                # rem = nums.copy()
                rem = list(nums)
                rem.remove(i)
                rec_res = dfs(rem)
                for perm in rec_res:
                    res.append([i]+perm)
            return res
        res1 = dfs(nums)
        return res1
