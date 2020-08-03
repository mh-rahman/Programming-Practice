class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starters = sorted([(x[0],i) for i,x in enumerate(intervals)])
        res = []
        
        for interval in intervals:
            # print(interval)
            s,e = interval
            if e > starters[-1][0]:
                # end point greater than the greatest starting point
                res.append(-1)
                continue
            pos = self.binSearch(starters, e)
            res.append(pos)
        return res
            
            
    def binSearch(self, starters, x):
        l,r = 0, len(starters)-1
        while l<r:
            mid = (l+r)//2
            if starters[mid][0] == x:
                return starters[mid][1]
            elif starters[mid][0] < x:
                l = mid+1
            else:
                r = mid
        return starters[r][1]
        