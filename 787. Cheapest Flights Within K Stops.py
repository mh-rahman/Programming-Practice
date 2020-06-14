class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #upto k stops -> no circles, can use less stops
        #Maintain visited array for lookup - to avoid cycles
        if src == dst:
            return 0
        
        costs = {i:{} for i in range(n)} #Dict of dictiionaries
        visited = [0]*n
        
        for s,d,c in flights:
            costs[s][d] = c
        
        for c in costs:
            costs[c] = {i:costs[c][i] for i in sorted(costs[c],key = lambda x:costs[c][x])}
        
        cheapest = math.inf

        Q = []
        heapq.heapify(Q) #Sort based on cost,stopnum,curr
        heapq.heappush(Q,[0,0,src])
        
        while Q:
            cost,stopnum,curr = heapq.heappop(Q)
            if curr == dst:
                cheapest = min(cheapest,cost)
                break
            if stopnum > K:
                continue
            visited[curr] = 1
            for c in costs[curr]:
                dest,price = c,costs[curr][c]
                temp = [cost+price,stopnum+1,dest]
                heapq.heappush(Q,temp)

        if cheapest == math.inf:
            cheapest = -1
        return cheapest