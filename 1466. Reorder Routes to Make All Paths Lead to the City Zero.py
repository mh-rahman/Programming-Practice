class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        canReach = set([0])
        # canReach.add(2)
        # print(len(canReach))
        count = 0
        while len(canReach) < n:
            #check which can be reached i.e road[1] == 0
            for i in range(len(connections)):
                road = connections[i]
                if road[1] == 0:
                    canReach.add(road[0]) 
                    
            #mark new reached, flip and count if needed [0,b] to [b,0]
            for i in range(len(connections)):
                road = connections[i]
                if road[1] in canReach:
                    road[1] = 0
                    continue
                if road[0] in canReach and road[1] != 0:
                    # print(road)
                    road[0], road[1] = road[1], 0
                    count+=1
            
            # print('canReach = ',canReach)
            # print('connections = ',connections)
            # print('count = ',count)
            
            
        
        return count
    