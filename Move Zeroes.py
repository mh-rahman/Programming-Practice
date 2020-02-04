class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # zero_pointer = 0
        # pointer = 0
        # l = len(nums)
        # while zero_pointer < l and pointer < l:
        #     # print(zero_pointer, pointer)
        #     if zero_pointer < pointer: nums[zero_pointer], nums[pointer] = nums[pointer], nums[zero_pointer]
        #     while nums[pointer] == 0:
        #         pointer+=1
        #         if pointer == l: return
        #     while nums[zero_pointer] != 0:
        #         zero_pointer+=1
        #         if zero_pointer == l: return
            
                
        nums.sort(key = bool, reverse = True)