from typing import List

class Solution:
    def iscycle(self, v, visited, recstack):
        visited[v] = True
        recstack[v] = True
        
        for neighbour in self.adj[v]:
            if not visited[neighbour]:
                if self.iscycle(neighbour, visited, recstack):
                    return True
            elif recstack[neighbour]:
                return True
        
        recstack[v] = False
        return False
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        self.adj = adj
        visited = [False] * V
        recstack = [False] * V
        
        for node in range(V):
            if not visited[node]:
                if self.iscycle(node, visited, recstack):
                    return True
        return False
