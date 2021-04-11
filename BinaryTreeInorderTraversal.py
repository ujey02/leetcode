# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #do it iteratively????
        candidates = []
        ans = []
        
        if root is None:
            return ans
        
        candidates.append(root)
        
        while candidates != []:
            curNode = candidates.pop()
            if hasattr(curNode, 'check'):
                ans.append(curNode.val)
            else:
                if curNode.right is not None:
                    candidates.append(curNode.right)
                candidates.append(curNode)
                if curNode.left is not None:
                    candidates.append(curNode.left)
                curNode.check = True
                    
        return ans
        
