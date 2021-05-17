class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxStep = nums[0]
        destStep = len(nums)-1
        idx = 1
        
        while idx < destStep:
            if idx <= maxStep:
                if idx + nums[idx] > maxStep:
                    maxStep = idx+nums[idx]
                idx += 1
            else:
                return False
        if maxStep >= destStep:
            return True
