class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l = len(T)
        if l<2:
            return [0]*l
        
        res = [0]*l
        i = l-1
        while i >= 0:
            j = i+1
            while j<l:
                if T[i]<T[j]:
                    res[i] = j
                    break
                if res[j] != 0:
                    j = res[j]
                else:
                    break
            
            i-=1
        
        res = [max(0,res[i]-i) for i  in range(l)]
        # print(res)
        
        return res