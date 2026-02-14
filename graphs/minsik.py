import sys
from collections import deque
input=sys.stdin.readline
class Edge():
    def __init__(self,u,v,w):
        self.fr=u
        self.to=v
        self.cost=w
n,start,end,m=map(int,input().split())
adj=[[] for _ in range(n)]
edges=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u].append((v,w));edges.append(Edge(u,v,w))
INF=float('INF')
dist=[-INF]*n
money=list(map(int,input().split()))
dist[start]=money[start]
for _ in range(n-1):
    for e in edges:
        if dist[e.fr]==-INF:
            continue
        val=dist[e.fr]+money[e.to]-e.cost
        if val>dist[e.to]:
            dist[e.to]=val
if dist[end]==-INF:
    print("gg")
    sys.exit(0)
cycle=[]
for e in edges:
    if dist[e.fr]==-INF:
        continue
    if dist[e.fr]+money[e.to]-e.cost>dist[e.to]:
        cycle.append(e.to)
visited=[False]*n;q=deque(cycle)
for x in cycle:
    visited[x]=True
while q:
    u=q.popleft()
    if u==end:
        print("Gee");sys.exit(0)
    for v in adj[u]:
        if not visited[v[0]]:
            visited[v[0]]=True;q.append(v[0])
print(dist[end])