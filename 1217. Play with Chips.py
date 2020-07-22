class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        min_cost = math.inf
        for pos in chips:
            #what if this is the position
            cost = 0
            for pos1 in chips:
                cost += abs(pos1-pos)%2
            min_cost = min(min_cost,cost)
            
        return min_cost