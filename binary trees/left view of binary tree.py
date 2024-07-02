#basically left view could also be part of tight child and hence bfs is done and the 0th child is added to the result 
def LeftView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        
        # Traverse all nodes of the current level
        for i in range(level_size):
            node = queue.popleft()
            
            # If this is the first node of the current level, add it to the result
            if i == 0:
                result.append(node.data)
            
            # Enqueue left child
            if node.left:
                queue.append(node.left)
            
            # Enqueue right child
            if node.right:
                queue.append(node.right)
    
    return result
