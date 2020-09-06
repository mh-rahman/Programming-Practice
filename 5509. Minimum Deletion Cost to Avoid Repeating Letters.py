class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # Greedy
        res = 0
        s = [c for c in s]
        i = 0
        while i < len(s)-1:
            cur, nxt = s[i], s[i+1]
            if cur == nxt:
                c1, c2 = cost[i], cost[i+1]
                if c1 > c2:
                    # delete next - swap cur, next
                    s[i], s[i+1] = nxt, cur
                    cost[i], cost[i+1] = c2, c1
                res += cost[i]
            i += 1
            
        return res