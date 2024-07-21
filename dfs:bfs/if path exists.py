#bfs approach
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph =[[] for _ in range(n)]

        for  e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        print(graph)
        visited=[False]*n
        visited[source]=True
        q=deque([source])    

        while q:
            tmp=q.popleft()
            if tmp==destination:
                return True
            for conn in graph[tmp]:
                if not visited[conn]:
                    visited[conn]=True
                    q.append(conn)
        return False                
