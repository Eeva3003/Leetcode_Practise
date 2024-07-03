class Solution:
    def isInside(self, x, y, N):
        return 1 <= x <= N and 1 <= y <= N

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]

        queue = []
        queue.append((KnightPos[0], KnightPos[1], 0))
        visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        visited[KnightPos[0]][KnightPos[1]] = True
        
        while queue:
            x, y, dist = queue.pop(0)
            
            if x == TargetPos[0] and y == TargetPos[1]:
                return dist
            
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                
                if self.isInside(new_x, new_y, N) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))
        
        return -1



class cell:

    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

# checks whether given position is
# inside the board


def isInside(x, y, N):
    if (x >= 1 and x <= N and
            y >= 1 and y <= N):
        return True
    return False

# Method returns minimum step to reach
# target position


def minStepToReachTarget(knightpos,
                         targetpos, N):

    # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []

    # push starting position of knight
    # with 0 distance
    queue.append(cell(knightpos[0], knightpos[1], 0))

    # make all cell unvisited
    visited = [[False for i in range(N + 1)]
               for j in range(N + 1)]

    # visit starting state
    visited[knightpos[0]][knightpos[1]] = True

    # loop until we have one element in queue
    while(len(queue) > 0):

        t = queue[0]
        queue.pop(0)

        # if current cell is equal to target
        # cell, return its distance
        if(t.x == targetpos[0] and
           t.y == targetpos[1]):
            return t.dist

        # iterate for all reachable states
        for i in range(8):

            x = t.x + dx[i]
            y = t.y + dy[i]

            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
