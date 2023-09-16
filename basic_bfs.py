from collections import deque

def bfs_by_queue(root):
    #root should be a list
    root = ['name','age','DOB']
    queue = deque(root) # at least one element in the queue to kick start bfs
    # print(queue)
    # exit()
    while len(queue) > 0: # as long as there is an element in the queue 
        node = queue.popleft() # dequeue from left to right
        # print(node)
        for child in node.children: # enqueue children
            if OK(child): # early return if problem condition met
                return FOUND(child)  # child here matches with our key for search
            queue.append(child)
    return NOT_FOUND

if __name__ == '__main__':
    root = ['name','age','DOB']
    bfs_by_queue(root)