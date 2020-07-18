class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <  10:
            return []
        s = [c for c in s]
        Q = deque([])
        lookup,res = set([]),set([])
        
        for i in range(10):
            Q.append(s[i])
            
        lookup.add(''.join(Q))
        for i in range(10, len(s)):
            Q.popleft()
            Q.append(s[i])
            curr = ''.join(Q)
            if curr in lookup:
                res.add(curr)
            else:
                lookup.add(curr)
                
        return res