#91.82 / 65.62

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer = []
        
        c1, c2 = 0, 0
        
        
        for i in range(m):
            nums1[-i-1] = nums1[m-1-i]
        
        idx = 0
        while c1 != m and c2 != n:
            e1, e2 = nums1[c1+n], nums2[c2]
            if e1 > e2:
                nums1[idx] = e2
                c2 += 1
            else:
                nums1[idx] = e1
                c1 += 1
            idx = c1+c2
            #print(e1,e2,nums1)
        
        for j in range(n-c2):
            nums1[idx+j] = nums2[c2+j]
        
#         while c1 != m and c2 != n:
#             e1, e2 = nums1[c1], nums2[c2]
#             if e1 > e2:
#                 answer.append(e2)
#                 c2 += 1
#             else:
#                 answer.append(e1)
#                 c1 += 1
        
#         print (c1,c2)
#         if m == c1:
#             answer = answer + nums2[c2:]
#         else:
#             answer = answer + nums1[c1:]
            
#         for i in range(len(answer)):
#             nums1[i] = answer[i]

#custom testcase
# [1,2,3,0,0,0]
# 3
# [2,5,6]
# 3
