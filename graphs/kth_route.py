import heapq
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
adj=[[] for _ in range(n+1)]
dist=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
hq=[]
heapq.heappush(hq,(0,1))
heapq.heappush(dist[1],0)
while hq:
    cost,u=heapq.heappop(hq)
    for v in adj[u]:
        c=cost+v[0]
        if len(dist[v[1]]) < k:
            heapq.heappush(hq,(c,v[1]))
            heapq.heappush(dist[v[1]],-c)
        elif c<-dist[v[1]][0]:
            heapq.heappop(dist[v[1]])
            heapq.heappush(hq,(c,v[1]))
            heapq.heappush(dist[v[1]],-c)
for i in range(1,n+1):
    print(-dist[i][0] if len(dist[i])==k else -1)