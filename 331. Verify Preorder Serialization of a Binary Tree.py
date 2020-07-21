class Solution:
    def isValidSerialization(self, p: str) -> bool:
        def helper(ind,p):
            k = ind
            if ind >= len(p):
                return False, ind
            if p[ind] == '#':
                return True,ind+1
            left,ind = helper(ind+1,p)
            if not left:
                return False,ind
            right,ind = helper(ind,p)
            if not right:
                return False,ind
            return True,ind
        
        if not p:
            return True
        p = p.split(',')
        res,ind = helper(0,p)
        return res and ind == len(p)
        