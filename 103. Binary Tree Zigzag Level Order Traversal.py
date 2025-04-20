from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root]) # always start with root)
        res = []
        level_idx = 0
        # res.append([root.val])

        while len(queue) > 0:
            level_zipzag = []
            level_idx += 1
            for _ in range(len(queue)):
                node = queue.popleft() # FIFO
                # idx += 1
                val = node.val
                # print(val, level_idx)
                level_zipzag.append(val)
                # if level_idx % 2 == 0 :
                #     print("odd")
                if node.left  : # odd num
                    queue.append(node.left)

                if node.right: # even num
                    queue.append(node.right)

            print("level_idx", level_idx, level_zipzag, res)
            if level_idx % 2 == 0 :
                print("even", level_zipzag[::-1])
                res.append(level_zipzag[::-1])
            else:
                res.append(level_zipzag)

        print(res)
        return res
