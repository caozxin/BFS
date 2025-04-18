### Breadth First Search on Trees
Breadth first search visits all nodes in a level before starting to visit the next level. BFS uses a queue (First In First Out). When we dequeue a node, we enqueue its children.

### DFS vs BFS
DFS is better at:
      Finding nodes far away from the root. 
BFS is better for:
      Finding nodes close/closest to the root. 

### Template
<img width="682" alt="image" src="https://github.com/user-attachments/assets/5b1c2deb-18ea-47c9-bc2a-ad795ca8225e" />


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
