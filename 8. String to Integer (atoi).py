class Solution:
    def myAtoi(self, ss: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -1*(2**31)
        
        res = 0
        s = 1
        flag = True
        flag2 = True
        lookup = [str(i) for i in range(10)]
        
        for c in ss:
            if flag2 and c == ' ':
                continue
            flag2 = False
            if flag:
                if c == '-':
                    s = -1
                flag = False
                if c == '-' or c == '+':
                    continue
            if c in lookup:
                res = res*10 + int(c)
            else:
                break
                
                
            
        res = s*res
        
        if res < INT_MIN:
            return INT_MIN 
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res