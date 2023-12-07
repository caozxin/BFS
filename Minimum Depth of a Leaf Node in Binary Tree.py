from lintcode import (
    TreeNode,
)
from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0
            
        queue = deque([root])
        result_list = []
        min_leaf_depth = float('inf') # this is a global variable
        curr_depth = 0 
        # while queue:
        while len(queue) > 0 :
            level = []
            curr_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                level.append(val)
                if not node.left and not node.right:
                    leaf = node
                    if curr_depth < min_leaf_depth:
                        min_leaf_depth = curr_depth
                    
                    print(leaf.val, min_leaf_depth)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result_list.append(level)


        # return len(result_list)
        return min_leaf_depth
