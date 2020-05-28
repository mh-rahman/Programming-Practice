class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        
        def checkRestPattern(pattern):
            i = 0
            # print('here',i,pattern)
            while i < len(pattern) - 1:
                if pattern[i] == '*' or pattern[i+1] == '*':
                    # print(i,'pass')
                    pass
                else:
                    # print('else')
                    return False
                i+=1
            if pattern[i] == '*':
                return True
            else:
                return False
            
        def helper(string, pattern):
            # print(string,pattern)
            idx = 0
            for i,p in enumerate(pattern):
                if idx >= len(string):
                    return checkRestPattern(pattern[i:])

                if i+1 < len(pattern) and pattern[i+1] == '*':
                    continue

                if p == '*':
                    if pattern[i-1] == '.':
                        flag = False
                        while idx <= len(string) and not flag:
                            flag = helper(string[idx:],pattern[i+1:])
                            idx+=1
                        return flag
                    elif pattern[i-1] == string[idx]:
                        temp = pattern[i-1]
                        flag = False
                        while idx<len(string) and string[idx] == temp and not flag:
                            flag = helper(string[idx:],pattern[i+1:])
                            idx+=1
                        if idx <= len(string) and not flag:
                            flag = helper(string[idx:],pattern[i+1:])
                        return flag
                    else:
                        continue
                if p == '.' or p == string[idx]:
                    print(idx,i, string,pattern)
                    idx+=1
                    
                else:
                    return False

            if idx == len(string):
                return True
            else:
                return False
            
                
        # print(string[len(string):])
        return helper(string, pattern)