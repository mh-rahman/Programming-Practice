class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        i1 = i2 = 0
        l1 = m
        l2 = n
        while i1<l1:
            if nums2[0] < nums1[i1]:
                nums2[0], nums1[i1] = nums1[i1], nums2[0]
                i1+=1
                i2 = 1
                while l2>1 and i2 < l2 and nums2[i2]<nums2[i2-1]:
                    nums2[i2],nums2[i2-1] = nums2[i2-1], nums2[i2]
                    i2+=1
            else:
                i1+=1
        
        i2 = 0
        while i2 < l2:
            nums1[l1] = nums2[i2]
            l1+=1
            i2+=1
            
        return
            
        
        
        
        
        
        