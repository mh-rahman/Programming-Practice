class Solution:
    def countBits(self, num: int) -> List[int]:
        
        count = [0]*(num+1)
        for i in range(1,num+1):
            if i%2 == 0:
                count[i] = count[i//2]
            else:
                count[i] = count[i//2]+1
                
        
        return count
                
        
        
        
        
        
        
        
        
        '''
        if n is power of 2, 
        if n is even, then return count(n/2)
        else return count(n/2)+1
        '''
        