class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def helper(ver1,ver2):
            if len(ver1) > len(ver2):
                return -1*helper(ver2,ver1)
            i = 0
            while i < len(ver1):
                if ver1[i] > ver2[i]:
                    return 1
                elif ver1[i] < ver2[i]:
                    return -1
                else:
                    i+=1
            
            if i == len(ver2):
                return 0
            else:
                return -1
            
        ver1 = [int(x) for x in version1.split('.')]
        ver2 = [int(x) for x in version2.split('.')]        
        
        #Remove trailing zeroes
        while ver1 and ver1[-1] == 0:
            ver1.pop()
            
        while ver2 and ver2[-1] == 0:
            ver2.pop()
            
        return helper(ver1,ver2)
    