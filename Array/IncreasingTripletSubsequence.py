class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # nums_length = len(nums)
        # if nums_length < 3:
        #     return False
        # first = nums[0]
        # second = None
#         #find second
#         for i in range(1,nums_length - 1):
#             num = nums[i]
#             if first < num:
#                 second = num
#                 nums = nums[i+1:]
#                 break
#             else:
#                 first = num
                
#         #find third
#         if second is None: #could not find second until now...
#             return False
        
#         else:
#             for num in nums:
#                 #print("find third >> cur: ", num, " first: ", first, " second: ", second)
#                 if num > second:
#                     return True
#                 if num > first:
#                     second = num
#                 elif num < first:
#                     first = num

        nums_length = len(nums)
    
        if nums_length < 3:
            return False
        second = None
        
        for i in range(1,nums_length-1):
            num = nums[i]
            if num > nums[0]:
                second = num
                break
            else:
                nums[0] = num
                
        if second is None: #could not find second until now...
             return False
            
        for j in range(i+1,nums_length):
            num = nums[j]
            print("find third >> cur: ", num, " first: ", nums[0], " second: ", second)
            if num > second:
                return True
            elif num > nums[0]:
                second = num
            elif num < nums[0]:
                nums[0] = num
        
        return False
