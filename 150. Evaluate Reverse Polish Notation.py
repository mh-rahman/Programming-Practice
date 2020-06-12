class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        func = {
            '+': lambda x,y : str(int(x) + int(y)), 
            '-': lambda x,y : str(int(x) - int(y)),
            '*': lambda x,y : str(int(x) * int(y)),
            '/': lambda x,y : str(int(x) // int(y)) if int(x) / int(y) > 0 else str(ceil(int(x) / int(y)))
        }
        
        idx = res = 0
        while idx < len(tokens):
            c = tokens[idx]
            if c in func.keys():
                y = stack.pop()
                x = stack.pop()
                stack.append(func[c](x,y))
            else:
                stack.append(c)
            idx+=1
        return stack[-1]