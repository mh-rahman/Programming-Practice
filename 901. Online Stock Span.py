class StockSpanner:

    def __init__(self):
        self.span = []
        self.price = []

    def next(self, price: int) -> int:
        # [100, 80, 60, 70, 60, 75, 85] -> [1, 1, 1, 2, 1, 4, 6]
        self.price.append(price)
        if not self.span or price < self.price[-2]:
            self.span.append(1)
        elif price == self.price[-2]:
            self.span.append(1 + self.span[-1])
        else:
            count, ind, l = 0, -1, len(self.span)
            while ind >= -l and price >= self.price[ind-1]:
                count += self.span[ind]
                ind -= self.span[ind]
            self.span.append(1 + count)
            
        # print(price, self.span)
        return self.span[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)