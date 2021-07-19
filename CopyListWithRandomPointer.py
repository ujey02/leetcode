"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        ans = Node(head.val)
        ans.idx = 0
        head.idx = 0
        
        copied = ans
        head2 = head
        
        nodes = {}
        nodes[0] = copied
        
        #copy initially 
        count = 1
        while head2.next is not None:
            copied.next = Node(head2.next.val)
            copied = copied.next
            head2 = head2.next
            
            copied.idx = count
            head2.idx = count
            nodes[count] = copied
            count += 1
        
        #copy random nodes by index
        copied = ans
        head2 = head
        
        while head2 is not None:
            if head2.random is not None:
                copied.random = nodes[head2.random.idx]
            else:
                copied.random = None
                
            copied = copied.next
            head2 = head2.next
                
        return ans
