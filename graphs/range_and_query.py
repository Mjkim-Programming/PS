import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
adj,rngs=[],[]
def can_go(a,b):
    visited=bfs(a-1)
    return visited[b-1]
def bfs(a):
    visited=[False]*len(rngs)
    visited[a]=True
    deq=deque([a])
    while deq:
        x=deq.popleft()
        for i in adj[x]:
            if not visited[i]:
                visited[i]=True
                deq.append(i)
    return visited
for _ in range(n):
    q,x1,y1=map(int,input().split())
    if q==1:
        idx=len(rngs)
        rngs.append((x1,y1))
        adj.append([])
        for i,v in enumerate(rngs[:-1]):
            x2,y2=v
            if (x2<x1 and x1<y2) or (x2<y1 and y1<y2):
                adj[idx].append(i)
            if (x1<x2 and x2<y1) or (x1<y2 and y2<y1):
                adj[i].append(idx)
    elif q==2:
        if can_go(x1,y1):
            print(1)
        else:
            print(0)