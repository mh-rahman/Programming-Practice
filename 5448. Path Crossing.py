class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        curr = [0,0]
        seen.add('0#0')
        lookup = {
            'N':[0,1],
            'S':[0,-1],
            'E':[1,0],
            'W':[-1,0],
        }
        
        for c in path:
            curr = [a+b for a,b in zip(curr,lookup[c])]
            x,y = curr
            pos = str(x)+'#'+str(y)
            if pos in seen:
                return True
            seen.add(pos)
            
        return False