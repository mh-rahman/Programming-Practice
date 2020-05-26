class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}
        for idx,num in enumerate(nums):
            if idx_dict.get(target-num,-1) != -1:
                return [idx_dict[target-num],idx]
            else:
                idx_dict[num] = idx
        
        return []