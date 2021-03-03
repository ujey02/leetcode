#53 / 98.75

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        tf = True
        search = [1,n]
        
        while search[0] != search[1]:
            cur = (search[1] + search[0])//2
            isBad = isBadVersion(cur)
            if isBad:
                search[1] = cur
            else:
                search[0] = cur + 1
            
        
        return search[0]
