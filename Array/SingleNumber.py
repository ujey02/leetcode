class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #solution for linear runtime w/o extra memory
        # if len(nums) == 1:
        #     return nums[0]
        # else:
        #     for i in range(1,len(nums)):
        #         nums[0] ^= nums[i]
        #     return nums[0]
        
        #faster solution
        if len(nums) == 1:
            return nums[0]
        else:
            return self.rec(nums, len(nums))
            
    def rec(self, nums, k):
        if k > 2:
            for i in range(k//2):
                #print ('hi')
                nums[i] ^= nums[k-i-1]
            return self.rec(nums,math.ceil(k/2))
        else:
            return nums[0]^nums[1]
