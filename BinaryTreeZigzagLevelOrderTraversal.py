# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        cand = Queue()
        if root is None:
            return ans
        
        isInverse = False
        
        cand.put(root)
        cand.put(None)
        level = []
        while not cand.empty():
            curNode = cand.get()
            if curNode is None:
                if isInverse:
                    level.reverse()
                    ans.append(level)
                    isInverse = False
                else:
                    ans.append(level)
                    isInverse = True
                if not cand.empty():
                    cand.put(None)
                    level = []
            else:
                level.append(curNode.val)
                if curNode.left is not None:
                    cand.put(curNode.left)
                if curNode.right is not None:
                    cand.put(curNode.right)
                    
        return ans
