import heapq
class Graph:
    def __init__(self, n, zb):
        """
        Initalize Graph
        
        :param n: Number of Nodes
        :param zb: Flag for zero-based(true if node indexing is zero-based)
        """
        self.n = n
        self.adj = [[] for _ in range(self.n)]
        self.zb = zb
        self.prev = [-1]*n
    def add_edge(self, at, to, w=1):
        if self.zb:
            self.adj[at].append((w, to))
        else:
            self.adj[at-1].append((w, to-1))
    def LazyDijkstra(self, at):
        if not self.zb:
            at = at - 1
        hq = []
        dist = [float('INF')]*self.n
        dist[at] = 0
        heapq.heappush(hq, (0, at))
        while hq:
            cd, u = heapq.heappop(hq)
            if cd > dist[u]:
                continue
            for w, v in self.adj[u]:
                nd = cd + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))
        return dist
    def LazyDijkstraToSNode(self, at, to):
        if not self.zb:
            at = at - 1
        if not self.zb:
            to = to - 1
        hq = []
        dist = [float('INF')]*self.n
        dist[at] = 0
        heapq.heappush(hq, (0, at))
        while hq:
            cd, u = heapq.heappop(hq)
            if cd > dist[u]:
                continue
            for w, v in self.adj[u]:
                nd = cd + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(hq, (nd, v))
            if u == to:
                return dist[to]
        return float('INF')
    def LazyMinRoute(self, at):
        if not self.zb:
            at = at - 1
        hq = []
        dist = [float('INF')]*self.n
        self.prev = [-1] * self.n
        dist[at] = 0
        heapq.heappush(hq, (0, at))
        while hq:
            cd, u = heapq.heappop(hq)
            if cd > dist[u]:
                continue
            for w, v in self.adj[u]:
                nd = cd + w
                if nd < dist[v]:
                    dist[v] = nd
                    self.prev[v] = u
                    heapq.heappush(hq, (nd, v))
        return dist, self.prev
    def restore_path(self, start, end):
        path = []
        cur = end
        while cur != -1:
            path.append(cur)
            if cur == start:
                break
            cur = self.prev[cur]
        path.reverse()
        return path
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