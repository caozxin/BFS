from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    print(root)
    if root:
        print("root has at least 1")


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    input = "1 2 4 x 7 x x 5 x x 3 x 6 x x"
    input02 = "x x x"
    root = build_tree(iter(input.split()), int)
    print(root)
    res = level_order_traversal(root)
    # for row in res:
    #     print(' '.join(map(str, row)))