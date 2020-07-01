class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        if len(nums) == 2:
            return True if sum(nums)%k == 0 else False
        dp = [n for n in nums]
        w = 2
        while w <= len(nums):
            i = 0
            while i+w <= len(nums):
                dp[i]+=nums[i+w-1]
                if dp[i]%k == 0:
                    # print(i,w)
                    return True
                i+=1
            # print(dp)
            w+=1
        return False