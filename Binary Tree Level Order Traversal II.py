from typing import (
    List,
)
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root: # always start with None handling! 
            return []
        queue = deque([root]) # always put [root] or a list[list[]] format when you initiate queue

        result_list = []

        while len(queue) > 0:
            pre_level = []

            for _ in range(len(queue)):

                node = queue.popleft() # queue can only popleft()

                print(node.val)
                pre_level.append(node.val)
                
                print("pre_level", pre_level)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            

            result_list.append(pre_level)
        result_list.reverse() # we is trying to reverse the path
        print("result_list", result_list)

        return result_list
