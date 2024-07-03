def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0
     
    # Consider every possible 
    # triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                 
                # check the triplet 
                # if it satisfies the condition
                if(i != j and i != k
                   and j != k and
                   g[i][j] and g[j][k] 
                   and g[k][i]):
                    count_Triangle += 1
     
    # If graph is directed , division is done by 3
    # else division by 6 is done
    if isDirected:
      return count_Triangle//3 
    else: return count_Triangle//6
