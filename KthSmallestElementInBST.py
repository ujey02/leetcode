# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        candidates = []
#         ans = []
        
#         if root is None:
#             return ans
        
        candidates.append(root)
        count = 0
        
        while candidates != []:
            curNode = candidates.pop()
            if hasattr(curNode, 'check'):
                count += 1
                if count == k:
                    return curNode.val
                # else:
                #     ans.append(curNode.val)
                
            else:
                if curNode.right is not None:
                    candidates.append(curNode.right)
                curNode.check = True
                candidates.append(curNode)
                if curNode.left is not None:
                    candidates.append(curNode.left)
                
                    
        # return ans[k-1]
