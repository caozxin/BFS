### Breadth First Search on Trees
Breadth first search visits all nodes in a level before starting to visit the next level. BFS uses a queue (First In First Out). When we dequeue a node, we enqueue its children.

### DFS vs BFS
DFS is better at:
      Finding nodes far away from the root. 
BFS is better for:
      Finding nodes close/closest to the root. 

<img width="623" alt="image" src="https://github.com/user-attachments/assets/d57f14e5-24ca-4064-8588-75a0cef4d747" />



      from collections import deque

      def bfs_by_queue(root):
          queue = deque([root]) # at least one element in the queue to kick start bfs
          while len(queue) > 0: # as long as there is an element in the queue
              node = queue.popleft() # dequeue
              for child in node.children: # enqueue children
                  if OK(child): # early return if problem condition met
                      return FOUND(child)
                  queue.append(child)
          return NOT_FOUND
