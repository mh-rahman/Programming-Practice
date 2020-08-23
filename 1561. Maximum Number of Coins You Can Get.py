class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse=True)
        n = len(piles)//3
        
        picks = [[piles[2*i], piles[2*i+1], piles[-i-1]] for i in range(n)]
        
        # print(piles)
        # print(picks)
        
        return sum([x[1] for x in picks])