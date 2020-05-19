class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        if l<2:
            return 0
        
        # i = 1
        # start = -1
        # while nums[i-1]<=nums[i]:
        #     if nums[i-1]!=nums[i]:
        #         start = i
        #     i+=1
        #     if i>=l:
        #         return 0
        # i-=1
        # if start == -1:
        #     start = i
        # max_ = nums[start]
        # end = start
        # i+=1
        # safe_max = -math.inf
        # while i<l:
        #     if nums[i]>=nums[i-1] and nums[i]>=max_:
        #         # print(i,nums[i],'safe')
        #         safe_max = max(safe_max, nums[i])
        #         # i+=1
        #     else:
        #         end = i
        #         max_ = max(max_,nums[i],safe_max)
        #         safe_max = -math.inf
        #         # i+=1
        #     print(i,nums[i],'Window = [', start,',', end,']\n max = ', max_, ' safe_max = ', safe_max)
        #     i+=1
            
        i = 0
        j = l-2
        start = l-1
        min_ = nums[start]
        end = 0
        max_ = nums[end]
        i+=1
        safe_max = -math.inf
        safe_min = math.inf
        while i<l and j>=0:
            if nums[i]>=nums[i-1] and nums[i]>=max_:
                safe_max = nums[i]
            else:
                end = i
                max_ = max(max_,nums[i],safe_max)
                safe_max = -math.inf
            if nums[j]<=nums[j+1] and nums[j]<=min_:
                safe_min = nums[j]
            else:
                start = j
                min_ = min(min_,nums[j],safe_min)
                safe_min = math.inf
            
            i+=1
            j-=1

        return max(end-start+1,0)