class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def getPivot():
            l = 0
            r = len(nums)-1
            while nums[l] > nums[r] and l<r:
                mid = (l+r)//2
                print(l,mid,r,':',nums[l], nums[mid], nums[r])
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def search(l,r):
            if target == nums[l]:
                return l
            # print(l,r)
            while l < r:
                # print(l,r)
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    r = mid
                else:
                    l = mid+1
            if target == nums[l]:
                return l
            return -1
        
        
        if not nums:
            return -1
        
        start = getPivot()
        # print(start)
        if target < nums[start] or target > nums[start-1]:
            return -1
        elif target <= nums[-1]:
            return search(start,len(nums)-1)
        else:
            return search(0,start-1)
        
            
        
        return -1