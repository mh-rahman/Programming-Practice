class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        l = len(gas)
        while False:
            # # deficit = [(gas[i]-cost[i],i) for i in range(l)]   
            # deficit = [gas[i]-cost[i] for i in range(l)]   
            # print(deficit)
            # for i in range(1,l):
            #     deficit[i]+=deficit[i-1]
            # print(deficit)
            # cumuGas = cumuCost = 0
            # idx = -1
            # for i in range(l):
            #     cumuCost+=cost[i]
            #     cumuGas+=gas[i]
            pass
        
        istart = 0
        
        while True:

            while istart < l:
                if gas[istart] >= cost[istart]:
                    break
                istart+=1

            # print(istart)
            if istart >= l:
                break

            idx = istart
            accugas = gas[idx]
            accucost = cost[idx]
            idx = (idx+1)%l

            while accugas >= accucost and idx != istart: 
                #complete one circle from start
                accugas += gas[idx]
                accucost += cost[idx]
                idx = (idx+1)%l

            if idx == istart:
                return idx

            #if chain breaks at idx
            if idx < istart:
                break
                
            istart = idx

        
        return -1