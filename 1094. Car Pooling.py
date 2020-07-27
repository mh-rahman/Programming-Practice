class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: (x[1],x[2]))
        passengers, dropHeap = 0, []
        heapq.heapify(dropHeap)
        for nPassengers, startLoc, endLoc in trips:
            #Drop passengers
            while dropHeap and dropHeap[0][0] <= startLoc:
                _, drop = heapq.heappop(dropHeap)
                passengers -= drop
            
            #Check capacity and return false
            if nPassengers + passengers > capacity:
                return False

            #Add to heap
            heapq.heappush(dropHeap,(endLoc, nPassengers))
            passengers += nPassengers
            
        return True