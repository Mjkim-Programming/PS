import sys
input=sys.stdin.readline
TC=int(input())
class Edge:
    def __init__(self,f,t,c):
        self.fr=f
        self.to=t
        self.cost=c
for _ in range(TC):
    n,m,w=map(int,input().split())
    edges=[]
    dist=[0]*n
    for _ in range(m):
        s,e,t=map(int,input().split())
        edges.append(Edge(s-1,e-1,t))
        edges.append(Edge(e-1,s-1,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        edges.append(Edge(s-1,e-1,-t))
    for i in range(n-1):
        for e in edges:
            if dist[e.fr]+e.cost<dist[e.to]:
                dist[e.to]=dist[e.fr]+e.cost
    flag=False
    for e in edges:
        if dist[e.fr]+e.cost<dist[e.to]:
            flag=True
            break
    print("YES" if flag else "NO")