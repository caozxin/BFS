from typing import (
    List,
)
# from lintcode import (
#     Point,
# )

# Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 

    description: Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, 
    find the shortest path to a destination position, return the length of the route.
    Return -1 if destination cannot be reached.
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        def if_within_grid(x, y, total_x, total_y) -> bool:
            return 0 <= x < total_x and 0 <= y < total_y
        

        move_directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


        total_y = len(grid)
        total_x = len(grid[0])


        input_x, input_y = source.x, source.y
        goal_x, goal_y = destination.x, destination.y

        queue = deque()
        queue.append((input_x, input_y, []))

        visited = set()
        while queue:
            curr_x, curr_y, path = queue.popleft()
            
            if curr_x == goal_x and curr_y == goal_y:
                path.append((curr_x, curr_y)) # only add the position to the path when it reachs the goal
                return len(path)-1
            if (curr_x, curr_y) not in visited:
                visited.add((curr_x, curr_y))


                for each_move in move_directions:
                    new_x = curr_x + each_move[0]
                    new_y = curr_y + each_move[1]

                    if if_within_grid(new_x, new_y, total_x, total_y) == True:
                        print((new_x, new_y), True)
                        if (new_x, new_y) not in visited and grid[new_y][new_x]== False:
                            new_path = path + [(curr_x, curr_y)] # for each move, we create new path
                            queue.append((new_x, new_y, new_path))
        return -1

    def shortest_path02(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        def if_within_grid(x, y, total_x, total_y) -> bool:
            return 0 <= x < total_x and 0 <= y < total_y

        move_directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        total_y = len(grid)
        total_x = len(grid[0])

        input_x, input_y = source.x, source.y
        goal_x, goal_y = destination.x, destination.y

        queue = deque()
        queue.append((input_x, input_y, 0))  # Store the x, y, and distance

        visited = set()
        while queue:
            curr_x, curr_y, distance = queue.popleft() # distance is a counter of how many nodes were visited in each path. If you want to know the path, you should add "path" instead of distance

            if curr_x == goal_x and curr_y == goal_y:
                return distance

            if (curr_x, curr_y) not in visited:
                visited.add((curr_x, curr_y))

                for each_move in move_directions:
                    new_x = curr_x + each_move[0]
                    new_y = curr_y + each_move[1]

                    if if_within_grid(new_x, new_y, total_x, total_y) == True:
                        if grid[new_y][new_x] == True: # this path is blocked
                            break
                        elif (new_x, new_y) not in visited and grid[new_y][new_x] == False: # we only visit the node if it is not blocked
                            queue.append((new_x, new_y, distance + 1))

        return -1

grid = [[0,1,0],[0,0,0],[0,0,0]]
[2,0]
[2,2]

source = Point(2, 0)
destination = Point(2,2)
new_solution = Solution()

result = new_solution.shortest_path02(grid, source, destination)
print("result", result)