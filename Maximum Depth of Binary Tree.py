from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here

        if not root:
            return 0

        queue = deque([root])
        max_depth = 0

        while len(queue) > 0:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                # max_depth += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth

