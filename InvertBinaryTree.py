# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Given the root of a binary tree, invert the tree, and return its root.

 
from collections import deque
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        queue = deque([root])  
        
        while queue:
            node = queue.popleft() 
            
            
            node.left, node.right = node.right, node.left
            
           
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root 
