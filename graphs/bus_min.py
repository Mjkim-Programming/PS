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
n = int(input())
m = int(input())
graph = Graph(n, False)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)
a, b = map(int, input().split())
dist, _ = graph.LazyMinRoute(a)
a -= 1
b -= 1
path = graph.restore_path(a, b)
print(dist[b])
print(len(path))
print(*[x+1 for x in path])