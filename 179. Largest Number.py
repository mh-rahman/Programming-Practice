class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def rank(s,largest):
            extension = max(ord(s[-1]),ord(s[0]))
            r = [extension]*largest
            idx = 0
            while idx < len(s):
                r[idx] = ord(s[idx])
                idx+=1
            while r and ceil(r[-1]) == 48:
                r.pop()
                if r:
                    r[-1]-=0.5
            return (r,len(s))
        
        nums = [str(n) for n in nums]
        largest = max(nums, key = lambda x: len(x))
        largest = len(largest)
        nums.sort(key = lambda x: rank(x,largest), reverse = True)
        result = ''.join(nums)
        idx = 0
        while idx < len(result) and result[idx] == '0':
            idx+=1
        idx = min(idx,len(result)-1)
        return result[idx:]