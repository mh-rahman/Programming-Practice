class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i,l,res = 0, len(nums), []
        while i < l:
            start,end = i,i
            while end+1 < l and nums[end+1] == nums[end]+1:
                end += 1
            if start == end:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[start])+'->'+str(nums[end]))
            i = end + 1
        return res