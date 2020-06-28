class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def helper(s,paths,visited):
            # print(s)
            destinations = paths.get(s,[])
            res,prev = [],""
            for i in range(len(destinations)):
                dst = destinations[i]
                if dst == "" or dst == prev:
                    continue
                paths[s][i] = ""
                # print('Going from ',s,'to',dst)
                res = helper(dst,paths,visited+1)
                # print(s,res)
                if res:
                    break
                prev = paths[s][i] = dst
            
            res.append(s)            
            if visited+len(res) == len(tickets)+1:
                # print(s,res,prev,"End")
                return res
            else:
                return []
        
        
        
        
        paths = {}
        for ticket in tickets:
            s,d = ticket
            if s in paths:
                paths[s].append(d)
            else:
                paths[s] = [d]
                
        for s in paths:
            paths[s].sort()
        # print(paths)
        res = helper('JFK',paths,0)
        
        return reversed(res)