import sys
input=sys.stdin.readline
class Edge:
    def __init__(self,f,t,c):
        self.fr=f
        self.to=t
        self.cost=c
n,m=map(int,input().split())
edges=[]
INF=float('INF')
dist=[INF]*n
dist[0]=0
for _ in range(m):
    s,e,t=map(int,input().split())
    edges.append(Edge(s-1,e-1,t))
for i in range(n-1):
    for e in edges:
        if dist[e.fr] != INF and dist[e.fr]+e.cost<dist[e.to]:
            dist[e.to]=dist[e.fr]+e.cost
flag=False
for e in edges:
    if dist[e.fr] != INF and dist[e.fr]+e.cost<dist[e.to]:
        flag=True
        break
if flag:
    print(-1)
else:
    for i in range(1,n):
        print(-1 if dist[i] == INF else dist[i])