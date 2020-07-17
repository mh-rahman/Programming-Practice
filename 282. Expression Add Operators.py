class Solution:
    res,target = [],0
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        def backtracking(idx=0, path='', value=0, prev=None):            
            if idx == len(num) and value == target:
                rtn.append(path)
                return
            
            for i in range(idx+1, len(num) + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    if prev is None :
                        backtracking(i, num[idx: i], tmp, tmp)
                    else:
                        backtracking(i, path+'+'+num[idx: i], value + tmp, tmp)
                        backtracking(i, path+'-'+num[idx: i], value - tmp, -tmp)
                        backtracking(i, path+'*'+num[idx: i], value - prev + prev*tmp, prev*tmp)
        
        rtn = []
        backtracking()

        return rtn
        
    def myAddOperators(self, num: str, target: int) -> List[str]:
        
        def evaluate(s):
            try:
                return eval(s) == self.target
            except:
                return False

        def dfs(constructed,ind,num):

            if ind >= len(num):
                
                if len(constructed) > 1 and constructed[0] == '0' and constructed[1] not in ['+','-','*']:
                    return
                i = 1
                while i < len(constructed)-1:
                    if constructed[i] == '0' and constructed[i-1] in ['+','-','*'] and constructed[i+1] not in ['+','-','*']:
                        return
                    i+=1
                
                s = ''.join(constructed)
                if evaluate(s):
                    self.res.append(s)
                return 
            
            for op in ['+','-','*']:
                constructed.append(op)
                constructed.append(num[ind])
                dfs(constructed,ind+1,num)
                constructed.pop()
                constructed.pop()
            
            constructed.append(num[ind])
            dfs(constructed,ind+1,num)
            constructed.pop()
            return
         
            
        if not num:
            return []
        self.res,self.target = [],target
        dfs([num[0]],1,num)
        
        return self.res
                
            