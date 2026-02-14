import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
MAX=100_000;dist=[-1]*(MAX+1);cnt=[0]*(MAX+1)
q=deque([n]);dist[n]=0;cnt[n]=1
while q:
    x=q.popleft()
    for nx in (x-1,x+1,2*x):
        if 0<=nx<=MAX:
            if dist[nx]==-1:
                dist[nx]=dist[x]+1;cnt[nx]=cnt[x]
                q.append(nx)
            elif dist[nx] == dist[x]+1:
                cnt[nx]+=cnt[x]
print(dist[k])
print(cnt[k])