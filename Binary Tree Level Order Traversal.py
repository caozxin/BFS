# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result_list = []
        queue = deque([root])
        level_order_num = 0
        # print(queue[0])
        
        while len(queue) > 0:
            level_order = []
            level_order_num += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                print(val)
                level_order.append(node.val)
                if node.left:
                    queue.append(node.left)
                    # level_order.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    # level_order.append(node.right.val)
                print("level_order", level_order)
            result_list.append(level_order)

        print("result_list", result_list)
        print("level_order_num", level_order_num)
        return result_list
