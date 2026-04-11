# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        #ensure p is smaller than q
        def traverse(node):
            if node.val < p.val:
                node = traverse(node.right)
            elif node.val > q.val:
                node = traverse(node.left)
            return node
        
        return traverse(root)