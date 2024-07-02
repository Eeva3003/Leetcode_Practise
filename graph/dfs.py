class Solution:
    def dfs(self, V, adj):
        # Step 1: Initialize the stack and visited array
        stack = []
        visited_arr = [False] * V
        dfs_traversal = []

        # Step 2: Start DFS from the first vertex (0)
        stack.append(0)
        visited_arr[0] = True
        
        # Step 3: Perform DFS traversal
        while stack:
            # Step 4: Pop a vertex from the stack
            vertex = stack.pop()
            dfs_traversal.append(vertex)
            
            # Step 5: Get all adjacent vertices of the popped vertex
            # If an adjacent vertex has not been visited, mark it visited and push it onto the stack
            for neighbour in reversed(adj[vertex]):
                if not visited_arr[neighbour]:
                    stack.append(neighbour)
                    visited_arr[neighbour] = True
        
        # Step 6: Return the DFS traversal list
        return dfs_traversal
