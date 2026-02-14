import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
adj=[[] for _ in range(n)]
edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    edges.append((c,a,b))
    adj[a].append((c,b))
    adj[b].append((c,a))
hq=[(0,0)]
visited=[False]*n
total,cnt,me=0,0,0
while hq and cnt<n:
    cost,nid=heapq.heappop(hq)
    if visited[nid]:
        continue
    visited[nid]=True
    total+=cost
    cnt+=1
    me=max(me,cost)
    for nc,nn in adj[nid]:
        if not visited[nn]:
            heapq.heappush(hq,(nc,nn))
print(total-me)