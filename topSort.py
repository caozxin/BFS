
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.

    description:
    Given an directed graph, a topological order of the graph nodes is defined as follow:
        For each directed edge A -> B in graph, A must before B in the order list.
        The first node in the order can be any node in the graph with no nodes direct to it.
    Find any topological order for the given graph.

    """
    def topSort(self, graph):
        # write your code here
        print