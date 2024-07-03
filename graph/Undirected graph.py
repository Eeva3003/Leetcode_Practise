#The approach used for detecting cycles in undirected graphs does not directly apply to directed graphs. This is because the logic relies on the fact that in undirected graphs, encountering a visited node that's not the parent indicates a cycle. However, in directed graphs,
#cycles can be more complex due to the direction of edges, and the notion of a "parent" does not apply the same way.from typing import List
#o detect cycles in directed graphs, we typically use the recursion stack (recstack) approach, as previously discussed, or employ algorithms like Kahn's algorithm for topological sorting
class Solution:
    def iscycleutil(self, v, visited, parent):
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all the vertices adjacent to this vertex
        for i in self.adj[v]:
            if not visited[i]:
                if self.iscycleutil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False
    
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        self.adj = adj
        visited = [False] * V
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for i in range(V):
            if not visited[i]:
                if self.iscycleutil(i, visited, -1):
                    return True
        return False       
		#Code here
