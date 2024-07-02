class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
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
                if i == level_size-1:
                    result.append(node.data)
            
            # Enqueue left child
                if node.left:
                    queue.append(node.left)
            
            # Enqueue right child
                if node.right:
                    queue.append(node.right)
    
        return result

        
    
        
