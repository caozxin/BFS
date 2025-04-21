from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #None handling:
        if not root:
            return [] # this should be matching the expected return format.

        queue = deque([root])
        res = []
        while len(queue) > 0: # it is true as long as we have root.
            level = []

            for _ in range(len(queue)): # this is the main loop.
                node = queue.popleft()
                val = node.val
                print("val", val)
                level.append(val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            print(" level", level)
            right_most = level.pop()
            print(" right_most", right_most)
            res.append(right_most)
        print(res)
        return res
