class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        opt = [1]*l
        i = l
        while i>0:
            i-=1
            prev = 0
            for j in range(i+1,l):
                if nums[j]>nums[i]:
                    prev = max(opt[j],prev)
            opt[i]+=prev
            # print(i,opt)
            
        return max(opt)
        