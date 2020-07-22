class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1:
            return 1
        ppl = {} #ppl: [trusts, trustedBy]
        for t in trust:
            a,b = t #a trusts b
            if a not in ppl:
                ppl[a] = [0,0]
            if b not in ppl:
                ppl[b] = [0,0]
            ppl[a][0] += 1
            ppl[b][1] += 1
            
        for p in ppl:
            if ppl[p] == [0,N-1]:
                return p
        
        return -1
        