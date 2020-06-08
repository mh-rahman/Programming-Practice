class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [0]*(amount+1)
        res[0] = 1
        for c in coins:
            for i in range(c,amount+1):
                res[i]+=res[i-c]
        return res[amount]