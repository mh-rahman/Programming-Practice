class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, xor2 = 0,1
        for n in nums: xor ^= n
        while xor%2 == 0:
            xor, xor2 = xor//2, xor2*2
        a,b = 0,0
        for n in nums:
            if n & xor2:
                a ^= n
            else:
                b ^= n
        return [a,b]
        
        