class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res
        res+=[[c] for c in nums]
        for _ in range(2**len(nums)):
            res+=[s+[c] for s in res for c in nums if s and c not in s and c>s[-1] and s+[c] not in res]
        # print(res)
            
        return res