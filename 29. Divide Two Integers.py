class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        else:
            sign = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            if sign > 0:
                return min(dividend,2**31-1)
            else:
                return max(-dividend,-2**31)
        
        quotient = 0
        # div = dividend
        div = divisor
        
        while dividend>=divisor:
            mul = 0
            count = 0
            while divisor+divisor<dividend:
                divisor = divisor+divisor
                mul+=1

            while dividend >= divisor:
                dividend-=divisor
                count+=1

            while mul:
                count = count+count
                mul-=1
            
            quotient+=count
            divisor = div
            
        
        if sign > 0:
            return min(quotient,2**31-1)
        else:
            return max(-quotient,-2**31)