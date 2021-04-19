# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        self.p = 0
        self.i = 0
        self.check = {}
        
        for val in preorder:
            self.check[val] = False
        
        return self.BTRec()
        
    def BTRec(self):
        if self.p == len(self.preorder):
            return None
        pVal = self.preorder[self.p]
        iVal = self.inorder[self.i]
        if not self.check[iVal]:
            self.p += 1
            node = TreeNode(pVal)
            self.check[pVal] = True
            if pVal != iVal:
                node.left = self.BTRec()
                node.right = self.BTRec()
            else:
                self.i += 1
                node.right = self.BTRec()
            return node
        else:
            self.i += 1
            return None

            
        
