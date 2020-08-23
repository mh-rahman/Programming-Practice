class PathCalculator:
    
    def __init__(self):
        # self.trips = set([])
        self.graph = {}
        self.longest_dist = 0
        self.longest_trip = ''
    
    def process(self, line: str) -> str:
        # print(line)
        line = line.split(':')
        city1, city2, dist = line
        dist = int(dist)
        # self.trips.add(':'.join(sorted([city1, city2])))
        if city1 not in self.graph:
            self.graph[city1] = {}
        if city2 not in self.graph:
            self.graph[city2] = {}
        
        self.graph[city1][city2] = dist
        self.graph[city2][city1] = dist
        
        if len(self.graph[city1]) == 1 and len(self.graph[city2]) == 1:
            return 'NONE'
        
        # get max distance using current cities
        curr_max_dist = 0
        if len(self.graph[city1]) > 1:
            # curr_max_dist = self.graph[city1][max(self.graph[city1], key = lambda k: self.graph[city1][k] if k != city2 else 0)]
            t1 = max(self.graph[city1], key = lambda k: self.graph[city1][k] if k != city2 else 0)
            t2 = city1
            t3 = city2
            curr_max_dist = self.graph[city1][t1]
            t1, t3 = sorted([t1,t3])
            
        if len(self.graph[city2]) > 1:
            # curr_max_dist = max(curr_max_dist, sef.graph[city2][max(self.graph[city2], key = lambda k: self.graph[city2][k] if k != city1 else 0)])
            temp = max(self.graph[city2], key = lambda k: self.graph[city2][k] if k != city1 else 0)
            if self.graph[city2][temp] > curr_max_dist:
                t1 = temp
                t2 = city2
                t3 = city1
                curr_max_dist = self.graph[city2][t1]
                t1, t3 = sorted([t1,t3])
        
        if dist + curr_max_dist > self.longest_dist:
            self.longest_dist = dist + curr_max_dist
            self.longest_trip = ':'.join([str(self.longest_dist), t1, t2, t3])
        
        return self.longest_trip
          