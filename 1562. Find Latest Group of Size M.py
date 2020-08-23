class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        # union set problem
        
        # parent = prev of index
        
        # maintain a dictionary of index, parent and length of 0's starting from parent
        # Should also have children - to update the parent value easily, when it itself get updated
        
        # while setting index i, if i-1 is set, then parent of i-1 will become parent of i and i will become child of parent of i-1
        # Increment lenght at parent by 1
        # Then, if i+1 is also set, exists in decitionary, then parent of i will become parent of i+1 and it's children
        # Increment lenght at parent index accordingly (using length of string i+1)
        # Delete i+1 from parent dictionary - save space
        
        # Three dictionaries: 
        # 1. Parent - children
        # 2. Children - parent
        # 3. Index - length
        
        
        getParent = {} #Children - parent
        getChildren = {} #Parent - children
        length = {} #Index - length
        mGroup = set() # Group of indices where length of m exists
        res = -1
                
        for step,ind in enumerate(arr):
            if ind-1 in getParent:
                p = getParent[ind-1]
                getParent[ind] = p
                getChildren[p].append(ind)
                length[p] += 1
            else:
                getParent[ind] = ind
                getChildren[ind] = [ind]
                length[ind] = 1
        
            p = getParent[ind]
            
            if ind+1 in getChildren:
                # absorb the string at i+1 into curr
                length[p] += length[ind+1]
                for child in getChildren[ind+1]:
                    getParent[child] = p
                    length[child] = length[p]
                getChildren[p] += getChildren[ind+1]
                del(getChildren[ind+1]) 
            
            
            if length[p] == m:
                mGroup.add(p)
            discarded = set()
            for k in mGroup:
                if length[k] != m:
                    discarded.add(k)
            mGroup = mGroup - discarded
            
            if len(mGroup) > 0:
                res = step+1

        # print(length)
        return res
        
    