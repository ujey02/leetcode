class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #get BST level
        if root is None:
            return root
        
#         parent = [root]
        
#         while parent[-1].left is not None:
#             child = []
#             for node in parent:
#                 if not child == []:
#                     child[-1].next = node.left
#                 node.left.next = node.right
#                 child.append(node.left)
#                 child.append(node.right)
#             child[-1].next = None
#             parent = child
        
# 97.85 % / 31.03 %
        parent = root
        
        while parent.left is not None:
            parent.left.next = parent.right
            prev_node = parent
            node = parent.next
            
            while node is not None: 
                prev_node.right.next = node.left
                node.left.next = node.right
                prev_node = node
                node = node.next
                
            prev_node.next = None
            parent = parent.left
        
        return root
