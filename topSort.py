
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.

    description:
    Given an directed graph, a topological order of the graph nodes is defined as follow:
        For each directed edge A -> B in graph, A must before B in the order list.
        The first node in the order can be any node in the graph with no nodes direct to it.
    Find any topological order for the given graph.

    graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
    [0, 1, 2, 3, 4, 5]

    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return 0

        #1) calculate the initial in_degree dict() for each node
        in_degree = dict((i, 0) for i in graph)
        for i in range(len(graph)):
   
            # print(graph[i].label)

            for each_neighbor in graph[i].neighbors:
                # print(each_neighbor.label)
                in_degree[each_neighbor] += 1 # you should directly add the node into dict()

        print(in_degree)

        #2) for those zero in-degree, we add them in the queue based on order
        queue = deque()
        for i in range(len(graph)):
            if in_degree[graph[i]] == 0:
                print(graph[i].label)
                queue.append(graph[i])

        #3) we empty the queue while adding the current node's neighbors into the queue
        result = []

        while queue:
            node = queue.popleft()
            print(node.label)
            result.append(node)
            for each_neighbor in node.neighbors:
                # print(each_neighbor.label)
                in_degree[each_neighbor] -= 1 # we first need to adjust the dependencies for current node's neighbors
                if in_degree[each_neighbor] == 0:
                    queue.append(each_neighbor) # only append the node to queue if it has zero in-degree

        return result # the expected output is a adjancy list of nodes. 

        

# new_solution = Solution()
# graph = [0,1,2,3,"#", 1,4, "#",2,4,5, "#", 3,4,5, "#",4, "#",5]
# # graph = list(graph)
# new_graph = DirectedGraphNode(graph[0])
# # print(new_graph.label)
# sum_list = []
# level_list = []
# for i in range(len(graph)):
#     # print(graph[i])
#     if graph[i] != "#":
#         level_list.append(graph[i])
#     elif graph[i] == "#":
#         sum_list.append(level_list)
#         # print(level_list)
        
#         level_list = []
    
# sum_list.append(level_list)
# # print(sum_list)

# for each_list in sum_list:
#     each_list[0] = new_graph.label
#     each_list[1:] = new_graph.neighbors

# # print(new_graph)
# result = new_solution.topSort(graph)
# print("result", result)