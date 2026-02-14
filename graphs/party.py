import sys
import heapq
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
n, m, x = map(int, input().split())
graph = Graph(n, False)
revGraph = Graph(n, False)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)
    revGraph.add_edge(v, u, w)
dist1 = graph.LazyDijkstra(x)
dist2 = revGraph.LazyDijkstra(x)
dist = [dist1[i]+dist2[i] for i in range(n)]
print(max(dist))