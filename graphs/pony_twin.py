import sys
from collections import deque
input=sys.stdin.readline
#TODO FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS
d,n,u,t=map(int,input().split())
N=(1<<d)-1
adj=[set() for _ in range(N+1)]
for i in range(2,N+1):
    p=i//2
    adj[i].add(p)
    adj[p].add(i)
for _ in range(n):
    s,e=map(int,input().split())
    adj[s].remove(e)
    adj[e].remove(s)
stk=[(1,0)]
visited=[False]*(N+1)
visited[1]=True
mdep,e=0,0
while stk:
    x,dep=stk.pop()
    for v in sorted(adj[x]):
        if not visited[v]:
            visited[v]=True
            stk.append((v,dep+1))
            mdep=dep+1
            e+=1
for i in range(N+1):
    visited[i]=False
ponytime=(2*e-mdep)*u
twintime=0
stk=[(1,0,0)]
visited[1]=True
while stk:
    x,dep,br=stk.pop()
    child=[]
    for v in adj[x]:
        if not visited[v]:
            child.append(v)
    if not child:
        twintime=max(twintime,dep*u+t*(br*(br-1)//2))
        continue
    if len(child)>=2:
        br+=1
    for c in child:
        visited[c]=True
        stk.append((c,dep+1,br))
if ponytime>twintime:
    print(":blob_twintail_aww:")
elif twintime>ponytime:
    print(":blob_twintail_sad:")
else:
    print(":blob_twintail_thinking:")
print(ponytime)
print(twintime)
#TODO FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS FIX THIS