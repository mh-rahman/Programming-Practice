class Solution:
    def isHappy(self, n: int) -> bool:
        def update(n):
            res = 0
            while n:
                temp = n%10
                n = n//10
                res+=(temp**2)
            return res
        
        visited = set([n])
        while True:
            n = update(n)
            # print(n)
            if n == 1:
                return True
            elif n in visited:
                return False
            visited.add(n)
            