from typing import (
    List,
)

from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer

    description:
    Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. 
    If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
    Find the number of islands.

    Input:
    [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [0,0,0,0,1]
    ]
    Output:
    3

    Input:
    [
    [1,1]
    ]
    Output:
    1
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        # once you find a "1", one queue should check if any 1 in its neighbor: up/down/left/right

        # def if_any_1_in_neighborhood(row, col):

        counter = 0
        row,col = 0, 0


        while row < len(grid) and col < len(grid[0]):
            queue = deque([])
            if grid[row][col] == 1:
                queue.append([row,col])
                grid[row][col] = 0 # update the val to 0
                counter += 1 # we add counter we found a root
                # print(grid)
                # print(queue)
                #then we check 4 directions:
                while len(queue) > 0:
                    for _ in range(len(queue)):
                        
                        node_row, node_col = queue.popleft()
                        # print("curr node: ", node_row, node_col)
                        
                        try:
                        #down:
                            if grid[node_row +1][node_col]:
                                if grid[node_row +1][node_col] == 1:
                                        queue.append([node_row+1,node_col])
                                        grid[node_row +1][node_col] = 0
                        except IndexError:
                            pass
                        try:
                            #up:
                            if grid[node_row -1][node_col]:
                                if grid[node_row -1][node_col] == 1:
                                        queue.append([node_row-1,node_col])
                                        grid[node_row -1][node_col] = 0
                        except IndexError:
                            pass
                        try:
                             #left:
                            if grid[node_row][node_col-1]:
                                if grid[node_row ][node_col-1] == 1:
                                        queue.append([node_row,node_col-1])
                                        grid[node_row ][node_col-1] = 0
                        except IndexError:
                            pass
                        try:
                        #right:
                            if grid[node_row][node_col+1]:
                                if grid[node_row][node_col+1] == 1:
                                        queue.append([node_row,node_col+1])
                                        grid[node_row ][node_col+1] = 0

                        except IndexError:
                            pass


            col += 1
            if col == len(grid[0]):
                 row += 1
                 col = 0

        
        return counter
                    


new_solution = Solution()
grid = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [0,0,0,0,1]
    ]
grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
    ]
result = new_solution.num_islands(grid)
print("result", result)