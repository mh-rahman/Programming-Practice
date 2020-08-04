class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## Greedy - interval scheduling from CLRS book
        
        intervals.sort(key = lambda x: (x[1], x[0]))
        # print(intervals)
        i, res = 0, 0
        while i < len(intervals)-1:
            # consider the one that finishes earliest and discard others that overlap with it
            curr_start, curr_end = intervals[i]
            i += 1
            while i < len(intervals):
                start, end = intervals[i]
                if start < curr_end <= end:
                    res += 1
                    i += 1
                else:
                    break
        return res
    
    
    def almostWorkingEraseOverlapIntervals(self, intervals1: List[List[int]]) -> int:
        
        ### remove duplicate entries
        intervals = list(set([(x[0], x[1]) for x in intervals1]))
        intervals.sort()
        print(len(intervals1))
        print(len(intervals))
        
        res = len(intervals1) - len(intervals)
        if len(intervals) < 2:
            return res
        
        graph = {} # ind: {indices of overlapping intervals}
        for i, interval in enumerate(intervals[:len(intervals)-1]):
            if i not in graph:
                graph[i] = set([])
            j = i+1
            s,e = intervals[j]
            while s < interval[1] <= e:
                graph[i].add(j)
                if j not in graph:
                    graph[j] = set([])
                graph[j].add(i)
                j += 1
                if j >= len(intervals):
                    break
                s,e = intervals[j]
        # print(graph)
        
        ind = max(graph, key = lambda x:len(graph[x]))
        while len(graph[ind]) > 0:
            # while overlapping exists
            res += 1
            neighbors = graph[ind]
            for n in neighbors:
                graph[n].remove(ind)
            del(graph[ind])
            # print('deleting ', ind)
            if not graph:
                break
            ind = max(graph, key = lambda x:len(graph[x]))
            # print(graph)
            
        return res
            
    
    def incompleteEraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # maintain a sorted list of start interval
        # binary search to pinpoint where curr can be inserted
        # check neighbors if curr is overlapping or not
        
        # Delete the interval with max overlaps
        # How to identify?
        
        # Graph - if overlap then branch exists. O(n**2) approach
        # heap: key = -(no. of edges)
        # a,b are sorted and are overlapping => b[0] < a[1] <= b[1]
        
        if len(intervals) < 2:
            return 0
        
        # graph = {} # ind: {indices of overlapping intervals}
        graph = [set([]) for i in intervals]
        intervals.sort()
        print(intervals)
        
        for i, interval in enumerate(intervals[:len(intervals)-1]):
            # if i not in graph:
            #     graph[i] = set([])
            
            j = i+1
            s,e = intervals[j]
            while s < interval[1] <= e:
                graph[i].add(j)
                # if j not in graph:
                #     graph[j] = set([])
                graph[j].add(i)
                j += 1
                if j >= len(intervals):
                    break
                s,e = intervals[j]
                
        graph = [(-len(x),i,x) for i,x in enumerate(graph)]
        graph.sort(reverse=True)
        # heapq.heapify(graph)
        while graph and graph[0][0] < 0:
            # while graph is not null and there is overlap
            # curr = heapq.heappop(graph)
            curr 
        return 0