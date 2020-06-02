class Solution:
    def maxSubArrayKadenes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = nums[0]
        maxCount = count
        for i in range(1,len(nums)):
            count = max(count,0)+nums[i]
            maxCount = max(maxCount,count)
            
        return maxCount
    
    def maxSubArray(self, nums: List[int]) -> int:
        def merge(ll,lr,rl,rr):
            # print(ll,lr,rl,rr)
            left = lr
            right = rl
            # if nums[left] > nums[right]:
            #     count = nums[left]
            #     left-=1
            # else:
            #     count = nums[right]
            #     right+=1
            # maxCount = count
            
            while False and count > 0:
                # # print(left,right)
                # if left<ll and right>rr:
                #     break
                # if left<ll:
                #     count = count+nums[right]
                #     right+=1
                # elif right>rr:
                #     count = count+nums[left]
                #     left-=1
                # else:
                #     if nums[left] > nums[right]:
                #         count += nums[left]
                #         left-=1
                #     else:
                #         count += nums[right]
                #         right+=1
                    
                maxCount = max(maxCount,count)
            
            cr = 0
            maxcr = -math.inf
            while right<=rr:
                cr+=nums[right]
                maxcr = max(maxcr,cr)
                right+=1
            
            cr = 0
            maxcl = -math.inf
            while left>=ll:
                cr+=nums[left]
                maxcl = max(maxcl,cr)
                left-=1
            maxCount = maxcl+maxcr
            
            return maxCount
                
        
        def helper(start,end):
            if end<=start:
                return nums[end]
            if end == start+1:
                return max(nums[start],nums[end],nums[start]+nums[end])
            # print(start,end)
            mid = (end+start)//2
            return max(helper(start,mid-1), helper(mid,end),merge(start,mid-1,mid,end))
            
        # print(merge(0,1,2,3))
        # return 0   
        if len(nums)<2:
            if nums:
                return nums[0]
            else:
                return 0
            
        return max(helper(0,len(nums)//2-1),helper(len(nums)//2, len(nums)-1),merge(0,len(nums)//2-1,len(nums)//2,len(nums)-1))
        