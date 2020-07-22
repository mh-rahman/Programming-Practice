class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p,zp,l = 0,0,len(nums)
        while p < l and zp < l:
            print(zp,p)
            while zp < l and nums[zp] != 0:
                zp += 1
            # p = zp+1
            while p < l and nums[p] == 0:
                p += 1
            if zp >= l or p >= l:
                print('OOR')
                break
            if p > zp:
                nums[zp], nums[p] = nums[p], nums[zp]
            else:
                p = zp+1

        # nums.sort(key = bool, reverse = True)