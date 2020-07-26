class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        def getIntersection(A,B):
            al,ah = A
            bl,bh = B
            if bl < al:
                return getIntersection(B,A)
            if bl > ah:
                return []
            return [bl,min(bh,ah)]
            
        
        a,b = 0,0
        res = []
        while a < len(A) and b < len(B):
            temp = getIntersection(A[a],B[b])
            if temp:
                res.append(temp)
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        return res
                