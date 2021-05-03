class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         ans = []
        
#         for n in nums:
#             if n in freq.keys():
#                 freq[n] += 1
#             else:
#                 freq[n] = 1
        
#         nKey = len(freq.keys())
        
#         if nKey/2 > 5:
#             for i in range(k):
#                 maxFreq = 0
#                 maxN = 0
#                 for key in freq.keys():
#                     if freq[key] > maxFreq:
#                         maxFreq = freq[key]
#                         maxN = key

#                 ans.append(maxN)
#                 del freq[maxN]

#         else:
#             for i in range(nKey-k):
#                 minFreq = 100001
#                 minN = 0
#                 for key in freq.keys():
#                     if freq[key] < minFreq:
#                         minFreq = freq[key]
#                         minN = key
#                 del freq[minN]
#             ans = freq.keys()
            
#         return ans
    
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         self.k = k
#         self.searchK = -1
        
#         for n in nums:
#             if n in freq.keys():
#                 freq[n] += 1
#             else:
#                 freq[n] = 1
        
#         sortFreq = self.quicksort(list(freq.items()))
#         return [f[0] for f in sortFreq[:k]]
        
#     def quicksort(self, items):
        
#         if len(items) < 2:
#             return items

#         pivot = items.pop()
#         left, right = [],[]
        
#         for item in items:
#             if item[1] >= pivot[1]: #large values go left, since we want the order to be decremental
#                 left.append(item)
#             else:
#                 right.append(item)
        
#         #recursively sort for left and right side of the array
#         leftSorted = self.quicksort(left)
#         rightSorted = self.quicksort(right)
        
#         return leftSorted + [pivot] + rightSorted
 
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        
        for n in nums:
            if n in freq.keys():
                freq[n] += 1
            else:
                freq[n] = 1
        
        sortFreq = self.mergesort(list(freq.items()))
        return [f[0] for f in sortFreq[:k]]

    def mergesort(self,items):
        num = len(items)
        if len(items) == 1:
            return items
        
        left = items[:round(num/2)]
        right = items[round(num/2):]
        
        items1 = self.mergesort(left)
        items2 = self.mergesort(right)
        
        return self.merge(items1,items2)
    
    def merge(self, items1, items2):
        p1,p2 = 0,0
        ans = []
        while p1 != len(items1) and p2 != len(items2):
            if items1[p1][1] > items2[p2][1]:
                ans.append(items1[p1])
                p1 += 1
            else:
                ans.append(items2[p2])
                p2 +=1
        
        if p1 == len(items1):
            ans += items2[p2:]
        else:
            ans += items1[p1:]
        
        return ans
        
        
        
