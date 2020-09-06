class Solution:
    def modifyString(self, s: str) -> str:
        res = []
        for i,c in enumerate(s):
            if c != '?':
                res.append(c)
                continue
            neighbors = []
            if i > 0:
                neighbors.append(res[-1])
            if i < len(s)-1:
                neighbors.append(s[i+1])
            # print(i, neighbors)
            for x in range(26):
                temp = chr(ord('a')+x)
                if temp not in neighbors:
                    res.append(temp)
                    break
                    
        # print(res)
        return ''.join(res)