class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digits, letters):
            if not digits:
                if not letters:
                    return None
                res.append(''.join(letters))
            else:
                temp = alphadict[digits[0]]
                for c in temp:
                    letters.append(c)
                    helper(digits[1:],letters)
                    letters.pop()
                    
            return
        
        res = []
        alphadict = {str(i):[] for i in range(1,10)}
        c = 0
        for num in range(2,10):
            count = c+3
            if num == 7 or num == 9:
                count = c+4
            while c < count:
                temp = ord('a')+num-2+c
                # print(num,chr(temp))
                alphadict[str(num)].append(chr(temp))
                c+=1
            c-=1
        # print(alphadict)
        helper(digits,[])
        return res
        