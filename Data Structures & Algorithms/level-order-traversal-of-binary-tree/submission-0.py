# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs, queue
        queue = deque()
        nodes = []
        if root:
            queue.append(root)
        
        while queue:
            print("new run")
            level_list = []
            for i in range(len(queue)):
                curr_node = queue.popleft()
                print(curr_node.val)
                level_list.append(curr_node.val)
                if curr_node:
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
            nodes.append(level_list)                 
        
        return nodes