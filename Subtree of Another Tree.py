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
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: #We first handle the base cases. If s is None, it means we have traversed the entire s tree, and t wasn't found as a subtree.
            return False

        if self.is_same_tree(s, t):
            return True

        print(s.val)
        #travel on parent tree s:

        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)
        #we first go through left_s_subtree if it is true, then we go through right_s_subtree

    def is_same_tree(self, s_subtree: TreeNode, t: TreeNode) -> bool:
        if not s_subtree and not t:  #if finish traveling both trees
            return True
        if not s_subtree or not t: #if only finish traveling one tree
            return False
        if s_subtree.val != t.val: # if any of node.val in s_subtree != t_node.val
            return False

        return self.is_same_tree(s_subtree.left, t.left) and self.is_same_tree(s_subtree.right, t.right)
        #to check if two trees are the same, we need to go through both left and right subtree



