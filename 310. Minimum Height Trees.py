class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        prev_leaves = leaves
        while leaves:
            new_leaves = []
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            prev_leaves, leaves = leaves, new_leaves

        return prev_leaves
    
    def bruteForceFindMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(root,graph):
            if root not in graph or len(graph[root]) == 0:
                return -1
            max_depth = 0
            children = graph[root]
            graph[root] = []
            for c in children:
                max_depth = max(max_depth, dfs(c,graph)+1)
            return max_depth
        
        if not edges:
            return [0]
        graph = {}
        for edge in edges:
            fr,to = edge
            if fr not in graph:
                graph[fr] = set([])
            graph[fr].add(to)
            if to not in graph:
                graph[to] = set([])
            graph[to].add(fr)
        g = graph.copy()
        
        height = {}
        for k in graph:
            g = graph.copy()
            height[k] = dfs(k,g)
        
        min_height = min(height.values())
        res = [k for k in graph if height[k] == min_height]
        
        return res