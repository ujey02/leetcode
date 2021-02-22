#76.55 / 61.35
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if self.isLeaf(root): return 1
        else:
            return self.rec(root)
    
    def isLeaf(self, node):
        if node.left == None and node.right == None:
            return True
        else:
            return False
        
    def rec(self, node):
        if node == None:
            return 0
        elif self.isLeaf(node): return 1
        else:
            left = self.rec(node.left)
            right = self.rec(node.right)
            return max(left,right) + 1
