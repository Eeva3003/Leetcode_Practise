    q = Queue()
        visited_arr  = [False]*V
        q.put(0)
        visited_arr[0] = True
        
        bfs_traversal = []
        
        while q.queue:
            
            vertex = q.get()
            bfs_traversal += [vertex]
            
            if len(adj[vertex]) > 0:
                for neighbour in adj[vertex]:
                    if not visited_arr[neighbour]:
                        q.put(neighbour)
                        visited_arr[neighbour] = True
                    
        return bfs_traversal
