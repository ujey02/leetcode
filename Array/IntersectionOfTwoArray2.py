class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect2(nums1,nums2)
        else:
            return self.intersect2(nums2,nums1)
        
    
    def intersect2(self, nums1,nums2):
        answer=[]
        n2 = len(nums2)
        count = 0
        for i in range(len(nums1)):
            a = nums1[i]
            for j in range(len(nums2)):
                if a == nums2[j]:
                    answer.append(nums2[j])
                    nums2[j] = -9999999
                    count += 1
                    if count == n2:
                        return answer
                    else:
                        break
        return answer
