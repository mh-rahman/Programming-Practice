class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums2)
        lookup = {nums2[i]:i for i in range(l)}
        for ind in range(len(nums1)):
            n,new = nums1[ind],-1
            i = lookup[n]
            for i in range(i+1, l):
                if nums2[i] > n:
                    new = nums2[i]
                    break
            nums1[ind] = new
        return nums1