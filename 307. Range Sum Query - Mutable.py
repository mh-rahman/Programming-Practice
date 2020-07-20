class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) <= 0:
            self.nums = None
            return
        self.nums = [0,nums[0]]
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            self.nums.append(nums[i])
        

    def update(self, i: int, val: int) -> None:
        diff = val - (self.nums[i+1] - self.nums[i])
        for i in range(i,len(self.nums)-1):
            self.nums[i+1] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1] - self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)