class Solution:
    def makeGood(self, s: str) -> str:
        s2 = s
        s = ''
        res = []
        
        while len(s) != len(s2):
            i = 0
            s = s2
            res = []
            while i <len(s)-1:
                c, c_ = s[i], s[i+1]
                if c != c_ and c.lower() == c_.lower():
                    i += 2
                else:
                    res.append(c)
                    i += 1
            if i < len(s):
                res.append(s[i])
            s2 = ''.join(res)
        #     print(s2)
        # print(res)
        return s2