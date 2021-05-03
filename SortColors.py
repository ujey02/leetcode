class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        
        #red (0)
        for i in range(n):
            if nums[i] == 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
                
        #white (1)
        for i in range(count, n):
            if nums[i] == 1:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
