class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            X, Y = nums1, nums2
        else:
            X, Y = nums2, nums1
            
        m, n = len(X), len(Y)
        total = (m + n + 1)//2
        start, end = 0, m
        
        
        import sys
        
        while start <= end:
            partX = (start+end)//2
            partY = (m + n + 1)//2 - partX
            
            # print (partX, partY)
            
            leftX = -1 * sys.maxsize if partX == 0 else X[partX-1]
            rightX = sys.maxsize if partX == m else X[partX]
            
            leftY = -1*sys.maxsize if partY == 0 else Y[partY-1]
            rightY = sys.maxsize if partY == n else Y[partY]
            
            # print(leftX, rightX, leftY, rightY)
            if leftX <= rightY and  leftY <= rightX:
                if (m+n)%2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY))/2
                else:
                    return max(leftX, leftY)
            elif leftX > rightY:
                end = partX - 1
            else:
                start = partX + 1
