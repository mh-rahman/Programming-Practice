class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        def binarySearch(l,r,target,flag = 0):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            if flag:
                return (l+r)//2
            return -1
            
        
        l = len(nums)
        if not nums or binarySearch(0,l-1,t,0) == -1:
            return [-1,-1]
        else:
            return [binarySearch(0,l-1,t-0.5,1)+1,binarySearch(0,l-1,t+0.5,1)]
        
