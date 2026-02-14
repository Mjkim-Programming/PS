import sys
import heapq
input=sys.stdin.readline
n=int(input())
planets=[]
for i in range(n):
    a,b,c=map(int,input().split())
    planets.append((a,b,c,i))
edges=[]
for d in range(3):
    planets.sort(key=lambda x: x[d])
    for i in range(n-1):
        a=planets[i][3]
        b=planets[i+1][3]
        cost=abs(planets[i][d]-planets[i+1][d])
        edges.append((cost,a,b))
adj=[[] for _ in range(n)]
for cost,a,b in edges:
    adj[a].append((cost,b))
    adj[b].append((cost,a))
visited=[False]*n
hq=[(0,0)]
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