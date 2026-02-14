import sys
import heapq
input=sys.stdin.readline
n=int(input())
adj=[[] for _ in range(n)]
edges=[]
for a in range(n):
    arr=list(map(int,input().split()))
    for b,c in enumerate(arr):
        if c==0:
            continue
        edges.append((c,a,b))
        adj[a].append((c,b))
        adj[b].append((c,a))
hq=[(0,0)]
visited=[False]*n
total,cnt=0,0
while hq and cnt<n:
    cost,nid=heapq.heappop(hq)
    if visited[nid]:
        continue
    visited[nid]=True
    total+=cost
    cnt+=1
    for nc,nn in adj[nid]:
        if not visited[nn]:
            heapq.heappush(hq,(nc,nn))
print(total)