class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: -abs(x[0]-x[1]))
        print(costs)
        cost = 0
        A = B = len(costs)//2
        i = 0
        
        while A>0 and B>0:
            a,b = costs[i][0],costs[i][1]
            if a<b:
                A-=1
                cost+=a
            else:
                B-=1
                cost+=b
            i+=1

        while A>0:
            a,b = costs[i][0],costs[i][1]
            A-=1
            cost+=a
            i+=1
        
        while B>0:
            a,b = costs[i][0],costs[i][1]
            B-=1
            cost+=b
            i+=1

        return cost
            