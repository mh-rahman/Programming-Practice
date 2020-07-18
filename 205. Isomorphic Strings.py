class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # flag = True
        lookup, charArray = {}, set([])
        for c1,c2 in zip(s,t):
            if (c1 in lookup and c2 != lookup[c1]) or (c1 not in lookup and c2 in charArray) :
                return False
            elif c1 not in lookup:
                lookup[c1] = c2
                charArray.add(c2)
        return True
                
        