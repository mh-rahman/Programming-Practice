class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def merge2(int1,int2):
            if int1[0] <= int2[0] and int2[0] <= int1[1]:
                return [[int1[0], max(int1[1],int2[1])]]
            else:
                return [int1,int2]
            
        if len(intervals) < 2:
            return intervals
        q = []
        res = []
        heapq.heapify(q)
        for i in intervals:
            heapq.heappush(q,i)        
        res.append(heapq.heappop(q))

        while q:
            temp1 = res.pop()
            temp2 = heapq.heappop(q)
            res+=merge2(temp1,temp2)
            # print(res, temp2)
            
            
        return res
        