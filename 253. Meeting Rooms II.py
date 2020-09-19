import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heapify(heap)
        res = 0        
        for interval in intervals:
            s,e = interval
            while heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            res = max(res, len(heap))
        return res
            