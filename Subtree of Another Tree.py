# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

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
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """

    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.is_same_tree(s, t):
            return True
        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: 
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False

        return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)
        
    

    def is_subtree_testing(self, s: TreeNode, t: TreeNode) -> bool:
        # Write your code here
        
        if not s or not t:
            return

        input_tree_one = s
        input_tree_two = t
        tree_one_root = s.val
        tree_two_root = t.val
        result = None

        # implement tree traversal:
        def dfs(input_tree_one: TreeNode, input_tree_two: TreeNode, tree_one_root, tree_two_root):
            if not input_tree_one or not input_tree_two: # this is the exist strategy
                return 
            print("before:")
            print(input_tree_one.val, input_tree_two.val)
            if input_tree_one.val == input_tree_two.val:
                #structure search starts:
                print(" the search starts")
                left = dfs(input_tree_one.left, input_tree_two.left, tree_one_root, tree_two_root)
                right = dfs(input_tree_one.right, input_tree_two.right, tree_one_root, tree_two_root)
                print(" during the search: ", input_tree_one.val, input_tree_two.val)
                if input_tree_one.val == tree_one_root or input_tree_two.val == tree_two_root:
                    print(" search ends!!!")
                    return True

            else:
                left = dfs(input_tree_one.left, input_tree_two,  tree_one_root, tree_two_root)
                right = dfs(input_tree_one.right, input_tree_two, tree_one_root, tree_two_root)
            print("after: ")
            print("     ", input_tree_one.val, input_tree_two.val)

            # return True

            if input_tree_one.val == input_tree_two.val:
                return True
            else:
                return False

        result = dfs(input_tree_one, input_tree_two, tree_one_root, tree_two_root)
        return result

