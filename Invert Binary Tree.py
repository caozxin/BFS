# Invert a binary tree.Left and right subtrees exchange.

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

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    note: this should be in place
    """
    def invert_binary_tree(self, root: TreeNode):
        # write your code here
        if not root:
            return None

        print(root.val)

        left = self.invert_binary_tree(root.left)
        right = self.invert_binary_tree(root.right)

        root.left, root.right = right, left

        return root
