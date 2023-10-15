from typing import (
    List,
)

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer

    tree = {1,2,3}
    output = [[1],[2,3]]

    tree = {1,#,2,3} 
    output = [[1],[2],[3]] 

    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:  # always check if root == None
            return []
        queue = deque([root])
        result_list = []
        
        # while queue:
        while len(queue) > 0 :  # do not hardcode the size here, since the size is changing when we popleft
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                level.append(val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result_list.append(level)


        print(result_list)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.left.left.left = TreeNode(-4)
# root.left.left.right = TreeNode(-5)
new_solution = Solution()
result = new_solution.level_order(root)
print("result", result)