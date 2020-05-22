class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = collections.Counter(nums1) - (collections.Counter(nums1) - collections.Counter(nums2))
        
        return list(res.elements())
