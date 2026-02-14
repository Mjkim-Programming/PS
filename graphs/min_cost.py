import heapq
import sys
input=sys.stdin.readline
class Graph:
    def __init__(self,n,zb):
        self.n=n
        self.adj=[[]for _ in range(self.n)]
        self.zb=zb
        self.prev=[-1]*n
    def add_edge(self,at,to,w=1):
        if self.zb:
            self.adj[at].append((w,to))
        else:
            self.adj[at-1].append((w,to-1))
    def LazyDijkstra(self,at):
        if not self.zb:
            at-=1
        hq=[]
        dist=[float('INF')]*self.n
        dist[at]=0
        heapq.heappush(hq,(0,at))
        while hq:
            cd,u=heapq.heappop(hq)
            if cd>dist[u]:
                continue
            for w,v in self.adj[u]:
                nd=cd+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(hq,(nd,v))
        return dist
n=int(input());m=int(input());g=Graph(n,False)
for _ in range(m):
    u,v,w=map(int,input().split());g.add_edge(u,v,w)
a,t=map(int,input().split())
d=g.LazyDijkstra(a);print(d[t-1])