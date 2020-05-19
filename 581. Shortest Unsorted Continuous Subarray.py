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
        end = 0
        max_ = nums[end]
        i+=1
        safe_max = -math.inf
        while i<l:
            if nums[i]>=nums[i-1] and nums[i]>=max_:
                # print(i,nums[i],'safe')
                safe_max = max(safe_max, nums[i])
                # i+=1
            else:
                end = i
                max_ = max(max_,nums[i],safe_max)
                safe_max = -math.inf
                # i+=1
            # print(i,nums[i],'max = ', max_, ' safe_max = ', safe_max)
            i+=1
        # print('End = ', end,'i.e.', nums[end])
            
        # print('\n\n\n')
        i = l-1
        start = l-1
        min_ = nums[start]
        i-=1
        safe_min = math.inf
        while i>=0:
            if nums[i]<=nums[i+1] and nums[i]<=min_:
                # print(i,nums[i],'safe')
                safe_min = min(safe_min, nums[i])
                # i+=1
            else:
                start = i
                min_ = min(min_,nums[i],safe_min)
                safe_min = math.inf
                # i+=1
            # print(i,nums[i],'min = ', min_, ' safe_min = ', safe_min)
            i-=1
        # print('start = ', start,'i.e.', nums[start])
            
            
            
        return max(end-start+1,0)