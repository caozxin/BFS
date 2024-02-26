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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.

    note: this should be in place
    """
    def is_identical(self, a: TreeNode, b: TreeNode) -> bool:
        # write your code here
        #1) None Handling:
        if not a and not b:
            return True
        elif not a or not b:
            return False
        print(a.val, b.val)
        #2) main loop:
        if a.val == b.val:
            left = self.is_identical(a.left, b.left)
            right = self.is_identical(a.right, b.right)
        
            if not left or not right:
                return False
        if a.val != b.val:
            return False
        
        return True
