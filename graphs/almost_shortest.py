from collections import deque
import heapq
import sys
input=sys.stdin.readline
class Graph:
    def __init__(self, n, zb):
        """
        Initalize Graph
        
        :param n: Number of Nodes
        :param zb: Flag for zero-based(true if node indexing is zero-based)
        """
        self.n = n
        self.adj = [[] for _ in range(self.n)]
        self.radj = [[] for _ in range(self.n)]
        self.zb = zb
        self.prev = [-1]*n
        self.banned = [[False]*n for _ in range(n)]
        self.dist = [-1]*n
    def add_edge(self, at, to, w=1):
        if self.zb:
            self.adj[at].append((w, to))
            self.radj[to].append((w, at))
        else:
            self.adj[at-1].append((w, to-1))
            self.radj[to-1].append((w, at-1))
    def LazyMinRoute(self, at):
        if not self.zb:
            at = at - 1
        hq = []
        self.dist = [float('INF')]*self.n
        self.prev = [-1] * self.n
        self.dist[at] = 0
        heapq.heappush(hq, (0, at))
        while hq:
            cd, u = heapq.heappop(hq)
            if cd > self.dist[u]:
                continue
            for w, v in self.adj[u]:
                if self.banned[u][v]:
                    continue
                nd = cd + w
                if nd < self.dist[v]:
                    self.dist[v] = nd
                    self.prev[v] = u
                    heapq.heappush(hq, (nd, v))
        return self.dist, self.prev
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
    def ban_shortest_path(self, at, to):
        if not self.zb:
            at -= 1
            to -= 1
        q = deque()
        q.append(to)
        visited = [False]*self.n
        visited[to] = True
        while q:
            v = q.popleft()
            for w, u in self.radj[v]:
                if self.dist[u] + w == self.dist[v]:
                    if not self.banned[u][v]:
                        self.banned[u][v] = True
                        if not visited[u]:
                            visited[u] = True
                            q.append(u)
n, m = map(int, input().split())
while n != 0 and m != 0:
    s, d = map(int, input().split())
    graph = Graph(n, True)
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)
    graph.LazyMinRoute(s)
    graph.ban_shortest_path(s, d)
    dist, _ = graph.LazyMinRoute(s)
    print(-1 if dist[d] == float('INF') else dist[d])
    n, m = map(int, input().split())