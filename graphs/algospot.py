import heapq
import sys
input=sys.stdin.readline
class GridGraph:
    def __init__(self, grid):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
    def LazyDijkstra(self, atx, aty):
        INF = 10**18
        dist = [[INF]*self.w for _ in range(self.h)]
        hq = []
        dist[atx][aty] = self.grid[atx][aty]
        heapq.heappush(hq, (dist[atx][aty], atx, aty))
        while hq:
            cd, x, y = heapq.heappop(hq)
            if cd > dist[x][y]:
                continue
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                if 0 <= nx < self.h and 0 <= ny < self.w:
                    nd = cd + self.grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(hq, (nd, nx, ny))
        return dist
m,n = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
graph = GridGraph(grid)
dist = graph.LazyDijkstra(0, 0)
print(dist[n-1][m-1])