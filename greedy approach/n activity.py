#greedy approach
def MaxActivities(arr, n): 
    selected = [] 
  
    # Sort jobs according to finish time 
    Activity.sort(key=lambda x: x[1]) 
  
    # The first activity always gets selected 
    i = 0
    selected.append(arr[i]) 
  
    for j in range(1, n): 
  
        '''If this activity has start time greater than or 
           equal to the finish time of previously selected 
           activity, then select it'''
        if arr[j][0] >= arr[i][1]: 
            selected.append(arr[j]) 
            i = j 
    return selected 
#priority queue approach - min heap
from heapq import heappop, heappush 
  
# Function to select activites 
  
  
def SelectActivities(s, f): 
    ans = [] 
    p = [] 
  
    # Pushing elements in the list 
    for i, j in zip(s, f): 
        heappush(p, (j, i)) 
  
    it = heappop(p) 
    start = it[1] 
    end = it[0] 
    ans.append(it) 
  
    # Sorting process 
    while p: 
        it = heappop(p) 
        if it[1] >= end: 
            start = it[1] 
            end = it[0] 
            ans.append(it) 
