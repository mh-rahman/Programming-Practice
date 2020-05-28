class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        lookup = {'I':['X','V'],'X':['C','L'],'C':['M','D']}
        i = len(s) - 1
        val = 0
        while i >= 0:
            c = s[i]
            if c in lookup.keys():
                if i+1 < len(s) and s[i+1] in lookup[c]:
                    val-=values[c]
                else:
                    val+=values[c]
            else:
                val+=values[c]
            i-=1
        return val