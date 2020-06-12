class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        ind = 0
        while ind < len(nums) and nums[ind] == 0:
            ind+=1
        red = ind - 1
        curr = ind
        blue = len(nums)
        while curr < blue and red < blue:
            # print(red,curr,blue)
            if red < curr and nums[curr] == 0:
                red+=1
                nums[red], nums[curr] = nums[curr], nums[red]
                while red < blue and nums[red+1] == 0:
                    red+=1
            elif nums[curr] == 2:
                blue-=1
                nums[blue], nums[curr] = nums[curr], nums[blue]
                while blue > 0 and nums[blue-1] == 2:
                    blue-=1
            else:
                curr = max(red,curr+1)
            # print(nums)
            
        return
        