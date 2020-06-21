class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l < 2:
            return 0
        
        reach, i = nums[0]-1, 1
        nreach, ni, jumps = 0, 0, 1
        
        while i < l-1:# and reach < l-1: # and idx >= 0:
            if i+nums[i] > nreach:
                nreach = i+nums[i]
                ni = i
            if reach <= 0:
                # print(nreach,i)
                reach = nreach - i
                jumps+=1
            i+=1
            reach-=1
        
        return jumps