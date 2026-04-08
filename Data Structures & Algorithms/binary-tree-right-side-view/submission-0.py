# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs
        queue = deque()
        if root:
            queue.append(root)
        rightsideview = []

        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node:
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
            rightsideview.append(curr_node.val)
        return rightsideview
