import sys
from collections import deque
input=sys.stdin.readline
class Edge():
    def __init__(self,fr,to,w):
        self.fr=fr
        self.to=to
        self.cost=w
n,m=map(int,input().split());INF=float('INF')
adj=[[] for _ in range(n+1)];dist=[INF]*(n+1);parent=[-1]*(n+1);edges=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    edges.append(Edge(u,v,-w))
    adj[v].append(u)
dist[1]=0
for _ in range(n-1):
    for e in edges:
        if dist[e.fr] != INF and dist[e.fr]+e.cost<dist[e.to]:
            dist[e.to]=dist[e.fr]+e.cost
            parent[e.to]=e.fr
cycle=[]
for e in edges:
    if dist[e.fr] != INF and dist[e.fr]+e.cost<dist[e.to]:
        cycle.append(e.to)
visited=[False]*(n+1);q=deque([n]);visited[n]=True
while q:
    u=q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v]=True;q.append(v)
for u in cycle:
    if visited[u]:
        print(-1)
        sys.exit(0)
cur=n;path=[]
while cur != -1:
    path.append(cur)
    cur=parent[cur]
path.reverse()
print(*path)