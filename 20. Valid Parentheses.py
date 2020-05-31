class Solution:
    def isValid(self, s: str) -> bool:
        openP = ['(', '[', '{']
        closeP = [')', ']', '}']
        pDict = {closeP[i]:openP[i] for i in range(3)}
        
        tempStack = []
        
        for c in s:
            
            if c in openP:
                tempStack.append(c)
            else:
                if not tempStack or tempStack.pop() != pDict[c]:
                    return False
                
                
        if not tempStack:
            return True
        else:
            return False