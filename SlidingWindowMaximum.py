class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

#         ##Time limit exceeded
#         ans = []
    
#         def findMax(nums,k,idx):
#             curMax = nums[idx]
#             for i in range(idx-k+1,idx):
#                 if nums[i] > curMax:
#                     curMax = nums[i]
#             return curMax
        
#         curMax = findMax(nums,k,k-1)
#         ans.append(curMax)
        
#         for j in range(k,len(nums)):
#             if nums[j] > curMax:
#                 curMax = nums[j]
#             elif nums[j-k] == curMax:
#                 curMax = findMax(nums,k,j)
#             ans.append(curMax)
            
#         return ans

        ##5000ms
        from queue import PriorityQueue
        que = PriorityQueue()
        check = {}
        for n in nums[:k]:
            que.put(-n)
            if n not in check:
                check[n] = 1
            else:
                check[n] += 1
                
        curMax = que.get() * -1
        ans = [curMax]
        
        for j in range(k, len(nums)):
            removeVal = nums[j-k]
            curVal = nums[j]
            check[removeVal] -= 1
            if curVal not in check:
                check[curVal] = 1
            else:
                check[curVal] += 1
            
            que.put(-curVal)

            if removeVal == curMax and check[removeVal] == 0:
                while True:
                    curMax = que.get() * -1
                    if check[curMax] > 0:
                        break
            
            if curMax < curVal:
                que.put(-curMax)
                curMax = que.get() * -1
                
            
            #print (curVal, curMax)
            ans.append(curMax)
                
        return ans
      
# ##best code from solution
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         curr_max = max(nums[:k])
#         max_window = [curr_max]
#         left = 0
#         for right in range(k, len(nums)):
#             left += 1
#             if nums[left - 1] == curr_max:
#                 if nums[left] >= curr_max - 1:
#                     curr_max = nums[left]
#                 else:
#                     curr_max = max(nums[left: right + 1])
#             curr_num = nums[right]
            
#             if curr_num > curr_max:
#                 curr_max = curr_num
#             max_window.append(curr_max)
            
#         return max_window
        
        
