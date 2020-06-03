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