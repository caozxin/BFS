# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return False
        result_list_p = []
        result_list_q = []

        def treeTraversal(root: Optional[TreeNode]) -> List:
            queue = deque([root])
            result_list = []

            while len(queue) > 0:
                node = queue.popleft()
                val = node.val
                print(val)
                result_list.append(val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return result_list

        result_list_p = treeTraversal(p)
        result_list_q = treeTraversal(q)
        print(result_list_p, result_list_q)

        if result_list_p == result_list_q:
            return True
        else:
            return False
        # return True
