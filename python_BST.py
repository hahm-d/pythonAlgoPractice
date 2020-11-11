# 700 Search in a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root:TreeNode, val:int):
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()            
            if node.val == val:                 #if it is equal return value
                return node            
            elif node.val > val:                # if current node is greater than target value, look left side of the tree
                if node.left:
                    stack.append(node.left)
            else:                               # if current node is less than target value, look right side of the tree
                if node.right:
                    stack.append(node.right)
        return None