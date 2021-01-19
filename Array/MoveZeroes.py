class Solution:
    #solution 1: 30/99
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for num in nums:
            if num != 0:
                if i != j:
                    nums[i] = num
                    nums[j] = 0
                i += 1
            j += 1


#     #solution 2: 23/-     
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums[:] = self.sub(nums,0, len(nums))
    
#     def sub(self, nums, ind, length):
#         if length == ind:
#             return []
#         for i in range(ind,length):
#             if nums[i] == 0:
#                 return nums[ind:i] + self.sub(nums,i+1,length) + [0]
#         return nums[ind:]
