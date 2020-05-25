class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.dup = self.original.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        del(self.dup)
        self.dup = self.original.copy()
        return self.dup
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.dup)
        return self.dup


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()