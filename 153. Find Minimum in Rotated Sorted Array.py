class Solution:
    def findMin(self, nums: List[int]) -> int:
        #pivot point between l,r if l>r
        #if mid > r, then pivot between mid and r
        
        l,r = 0, len(nums)-1
        while l <= r and nums[l] > nums[r]:
            if l == r:
                break
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
                
        return nums[l]
            
