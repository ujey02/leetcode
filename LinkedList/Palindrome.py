#https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

# # 40 / -
#     def isPalindrome(self, head: ListNode) -> bool:
#         if head is None or head.next is None:
#             return True
#         return self.rec(head.next, head)[0]
    
#     def rec(self, node, forNode):
#         if node.next is None:
#             return node.val == forNode.val, forNode.next
#         else:
#             tf, nextNode = self.rec(node.next, forNode)

#             if tf:
#                 return node.val == nextNode.val, nextNode.next
#             else:
#                 return tf, ""

## 14 / 9
#     def isPalindrome(self,head: ListNode) -> bool:
#         tail = None
#         curNode = head
#         while curNode is not None:
#             node = ListNode(curNode.val, tail)
#             tail = node
#             curNode = curNode.next
        
#         while head is not None:
#             if head.val != tail.val:
#                 return False
#             else:
#                 head = head.next
#                 tail = tail.next
#         return True

# # - / 93.61
#     def isPalindrome(self, head: ListNode) -> bool:
#         fw = 0
#         bw = 0
#         mul = 1
#         while head is not None:
#             fw = head.val + fw*10 
#             bw = head.val * mul + bw
#             mul *= 10
#             head = head.next
#         return fw == bw

# 99 (60) / 99
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        
        for i in range((len(stack)+1)//2):
            if stack[i] != stack[-1-i]:
                return False
        return True
                
            
        
