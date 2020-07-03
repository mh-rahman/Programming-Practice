class Solution:
    def isPalindrome(self, x: int) -> bool:
        mul = 1
        
        if x < 0:
            return False
        
        while mul*10 <= x:
            mul*=10
        
        while mul > 1:
            left = x//mul
            right = x%10
            # print(x,left,right,mul)
            if left != right:
                return False
            x = x%mul
            x = x//10
            mul = mul//100
            
        return True