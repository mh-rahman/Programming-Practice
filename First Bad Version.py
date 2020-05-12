# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    
    
    def firstBadVersion(self, n):
        def findBadVersion(start, end):
            if start==end:
                return start

            version = (start+end)//2
            if isBadVersion(version):
                return findBadVersion(start,version)
            else:
                return findBadVersion(version+1,end)
        """
        :type n: int
        :rtype: int
        """
        return findBadVersion(1, n)
        

        