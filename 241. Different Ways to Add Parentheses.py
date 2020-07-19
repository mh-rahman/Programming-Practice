class Solution:

        
    def diffWaysToCompute(self, input, memo={}):
        '''
        :type input: str
        :rtype: List[int]

        The dict memo={} is actually created 
        only once when the method diffWaysToCompute
        is instantiated. It behaves like a static object.
        '''
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n