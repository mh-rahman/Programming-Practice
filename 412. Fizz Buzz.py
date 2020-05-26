class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1,n+1):
            if num >= 15 and num%15 == 0:
                res.append('FizzBuzz')
            elif num >=5 and num%5 == 0:
                res.append('Buzz')
            elif num >= 3 and num%3 == 0:
                res.append('Fizz')
            else:
                res.append(str(num))
                
        return res
        