# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "[]"
        searchSpace = [root]
        serialized = ""
        while len(searchSpace) > 0 and len(searchSpace) > searchSpace.count(None):
            curNode = searchSpace.pop(0)
            if isinstance(curNode,TreeNode):
                if not serialized == "":
                    serialized += ","
                serialized += str(curNode.val)
                left = curNode.left
                right = curNode.right
                searchSpace.append(left)
                searchSpace.append(right)
            else:
                serialized+=",null"
        
        return "[" + serialized + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        
        sArray = data[1:-1].split(",")
        rootVal = sArray.pop(0)
        root = TreeNode(rootVal)
        searchSpace = [root]
        while not len(sArray) == 0:
            curNode = searchSpace.pop(0)
            if not len(sArray) == 0:
                left = sArray.pop(0)
                if left == "null":
                    curNode.left = None
                else:
                    leftNode = TreeNode(left)
                    curNode.left = leftNode
                    searchSpace.append(leftNode)
            if not len(sArray) == 0:
                right = sArray.pop(0)
                if  right == "null":
                    curNode.right = None
                else:
                    rightNode = TreeNode(right)
                    curNode.right = rightNode
                    searchSpace.append(rightNode)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
