class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        remEmpty = 0
        while numBottles:
            drink += numBottles
            numBottles += remEmpty
            remEmpty = numBottles%numExchange
            numBottles = numBottles//numExchange
            
        return drink