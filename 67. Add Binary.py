class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b,a)
        
        res = []
        i, carry = 0, 0
        
        while i < len(b):
            a1, a2 = a[len(a)-1-i],b[len(b)-1-i]
            if a1 == '1' and a2 == '1':
                s = 2+carry
            elif a1 == '0' and a2 == '0':
                s = carry
            else:
                s =  carry + 1
            res.append(str(s%2))
            carry = s//2
            i+=1
            
        while i < len(a):
            s = int(a[len(a)-1-i])+carry
            res.append(str(s%2))
            carry = s//2
            i+=1
            
        if carry > 0:
            res.append(str(carry))

        return ''.join([str(x) for x in reversed(res)])