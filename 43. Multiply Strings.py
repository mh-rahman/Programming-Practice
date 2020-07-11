class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.multiply(num2, num1)
        
        if num2 == '0' or num1 == '0':
            return '0'
        
        prev_res = []
        res = []
        # for ind in range(len(num2)):
        for ind in range(len(num2)):
            mul = int(num2[len(num2)-1 - ind])
            carry = 0
            res = [0]*ind
            ##keep appending to res and then reverse it at the end
            for i in range(len(num1)):
                num = int(num1[len(num1)-1 - i])
                product = mul*num + carry
                res.append(product%10)
                carry = product//10
                    
            if carry > 0:
                res.append(carry)
            # res = res[::-1]
            i = carry = 0
            while i < len(prev_res):
                s = prev_res[i] + res[i] + carry
                s,carry = s%10, s//10
                res[i] = s
                i+=1
            
            if carry > 0:
                if i < len(res):
                    res[i]+=carry
                else:
                    res.append(carry)
            # print(res)
            del(prev_res)
            prev_res = res
            
        return ''.join([str(x) for x in reversed(res)])

                
            