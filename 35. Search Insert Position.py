class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if r <= l:
                if target <= nums[l]:
                    return l
                else:
                    return l+1
            else:
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    return helper(l,mid-1)
                else:
                    return helper(mid+1,r)
        if nums:
            return helper(0,len(nums)-1)
        else:
            return 0