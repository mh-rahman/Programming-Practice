class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        sectors = [[i+1,0] for i in range(n)]
        start = rounds[0]
        for end in rounds[1:]:
            i = start # sector_id - 1
            while i != end:
                # print(start, end, i)
                sectors[i-1][1] += 1
                i = max(1,(i+1)%(n+1))
            start = end
        
        sectors[start-1][1] += 1 # also visit the end most sector
        # print(sectors)
        
        sectors.sort(key= lambda x: x[1]) # sort based on number of visits
        maxVisits = sectors[-1][1]
        res = [x[0] for x in sectors if x[1] == maxVisits]
        
        return res