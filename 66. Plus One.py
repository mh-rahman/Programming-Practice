class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry:
            if i < 0:
                return [1]+digits
            temp = digits[i]+carry
            if temp<10:
                digits[i] = temp
                carry = 0
            else:
                digits[i] = temp - 10
            i-=1
        return digits
                