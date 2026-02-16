import sys
from collections import deque
input=sys.stdin.readline
n,e=map(int,input().split())
adj=[[] for _ in range(n)]
for _ in range(e):
    a,b,v=map(int,input().split())
    adj[a].append((b,v))
    adj[b].append((a,v))
deq=deque([(0,0,0),(0,0,1)])
visited1=[False]*n
visited2=[False]*n
visited1[0]=True
visited2[0]=True
mindepth=-1
while deq:
    x,depth,b=deq.popleft()
    if x==n-1:
        mindepth=depth
        break
    for to,v in adj[x]:
        if v!=b:
            if v==0:
                if not visited1[to]:
                    visited1[to]=True
                    deq.append((to,depth+1,0 if b==1 else 1))
            else:
                if not visited2[to]:
                    visited2[to]=True
                    deq.append((to,depth+1,0 if b==1 else 1))
print(mindepth)
