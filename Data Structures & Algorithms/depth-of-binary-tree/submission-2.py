# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs
        stack = []
        maxdepth = 0
        stack.append([root, 1])

        while stack:
            curr_node, curr_depth = stack.pop()
            if curr_node:
                if curr_node.right:
                    stack.append([curr_node.right,curr_depth+1])
                if curr_node.left:
                    stack.append([curr_node.left, curr_depth+1])
                maxdepth = max(maxdepth, curr_depth)
        return maxdepth
            