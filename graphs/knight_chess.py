from collections import deque
import sys
input=sys.stdin.readline

def solve():
    """
    Solve the problem by BFS
    """
    I = int(input())
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())

    grid = [[-1] * I for _ in range(I)]
    grid[cx][cy] = 0

    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    # I tried managing two queues for each coordinates
    xq = deque([cx])
    yq = deque([cy])

    while xq:
        x, y = xq.popleft(), yq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            """
            Using the grid array as visited array. If the cell was already visited, it has distance in it.
            """
            if 0 <= nx < I and 0 <= ny < I and grid[nx][ny] == -1:
                xq.append(nx)
                yq.append(ny)
                grid[nx][ny] = grid[x][y] + 1

    print(grid[tx][ty])
    
T = int(input())
for _ in range(T):
    solve()