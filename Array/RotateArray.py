class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k%len(nums) != 0:
            k %= len(nums)
            # for i in range(k):
            #     n = nums.pop(-1)
            #     nums.insert(0,n)
            
            a = nums[-k:]
            b = nums[:-k]

            nums[:k+1] = a
            nums[k:]=b

            # for i in range(len(nums)-k):
            #     n = nums.pop(0)
            #     nums.append(n)
