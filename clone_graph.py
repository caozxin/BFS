# from lintcode import (
#     UndirectedGraphNode,
# )


# Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

from collections import deque
class Solution:
    """
    @param node: A list of undirected graph node
    @return: A undirected graph node

    description: Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.
    You need to return a deep copied graph, which has the same structure as the original graph, 
    and any changes to the new graph will not have any effect on the original graph.

    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here

        if not node:
            return None
            
         #1) find and copy all the nodes by BFS
        input_node = node
        queue = deque([node])
        visited = {} # Keep track of visited nodes
        while queue:
            node = queue.popleft()
            # print(node.label)
            if node in visited:
                pass

            visited[node] = UndirectedGraphNode(node.label)

            if node.neighbors:
                # visited[node].neighbors = node.neighbors
                for each_neighbor in node.neighbors:# please note this is while loop base case
                    if each_neighbor not in visited: 
                        queue.append(each_neighbor)

        # 2) Copy all the edges (neighbors)
        for each_node in visited:
            new_node = visited[each_node]
            for neighbor in each_node.neighbors:
                new_node.neighbors.append(visited[neighbor]) # because visited is a dict(), it could be called independently. 

        return visited[input_node]

    def clone_graph_default(self, node: UndirectedGraphNode) -> UndirectedGraphNode:

        if not node:
            return None

        # 1) Find all the nodes by BFS
        input_node = node
        result = []
        queue = deque([node])
        visited = {}  # Keep track of visited nodes

        while queue:
            current_node = queue.popleft()

            if current_node in visited:
                continue  # Skip if already visited

            visited[current_node] = UndirectedGraphNode(current_node.label)
            result.append(visited[current_node])

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        # 2) Copy all the edges (neighbors)
        for original_node in visited:
            new_node = visited[original_node]
            for neighbor in original_node.neighbors:
                new_node.neighbors.append(visited[neighbor])

        return visited[input_node]



# Create nodes
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(4)
# node4 = UndirectedGraphNode(4)

# Connect nodes (create edges)
node1.neighbors.append(node2)  
node1.neighbors.append(node3)
node2.neighbors.append(node3) 
node2.neighbors.append(node1) 
node3.neighbors.append(node1)
node3.neighbors.append(node2) 
node_list = list({node1, node2, node3})
# Now you have created a simple undirected graph with 3 nodes and 3 edges.
new_solution = Solution()
result = new_solution.clone_graph(node_list)
print(result)