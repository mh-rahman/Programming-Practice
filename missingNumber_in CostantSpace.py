class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        foundZero = False
        nums.append(l)
        for i in range(l):
            if nums[abs(nums[i])] == 0:
                foundZero = True
            else:
                nums[abs(nums[i])]=-abs(nums[abs(nums[i])])
        print(nums)
        for i,x in enumerate(nums):
            if x == 0 and not foundZero:
                return i
            if x > 0:
                return i
        # return False