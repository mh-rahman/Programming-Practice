class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        maxN, l = max(nums), len(nums)
        res = [-1]*l
        if nums[-1] != maxN:
            for i,n in enumerate(nums):
                if n > nums[-1]:
                    res[-1] = i
                    break
        for ind in range(l-2,-1,-1):
            n = nums[ind]
            if n == maxN:
                continue
            i = ind+1
            while True:
                if nums[i] > n:
                    res[ind] = i
                    break
                elif nums[i] == n and res[i] != -1:
                    res[ind] = res[i]
                    break
                elif res[i] != -1:
                    i = res[i]
                else:
                    i += 1
        res = [nums[i] if i >= 0 else -1 for i in res]
        return res