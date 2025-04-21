from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        #none handling:
        if not root:
            return 0 # this needs to be matching expected return format.

        queue = deque([root])
        # res = []
        level_idx = 0

        while len(queue) > 0: # this is true as long as we have root.
            # level = []
            level_idx += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                # level.append(val)
                # print(val, level_idx)
                # level_idx += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return level_idx
