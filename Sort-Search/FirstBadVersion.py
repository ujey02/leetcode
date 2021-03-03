#53 / 46

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
                search = [search[0], cur]
            else:
                search = [cur + 1, search[1]]
            
        
        return search[0]
