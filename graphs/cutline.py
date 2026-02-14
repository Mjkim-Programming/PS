import sys
input=sys.stdin.readline
v,e=map(int,input().split())
idv,n=0,v
adj=[[] for _ in range(v)]
ids,low,visited=[0]*n,[0]*n,[False]*n
for _ in range(e):
    u,v=map(int,input().split())
    u-=1;v-=1;
    adj[u].append(v)
    adj[v].append(u)
def bridge():
    global idv
    bridges=set()
    for s in range(n):
        if visited[s]:
            continue
        stk=[(s,-1,0)]
        visited[s]=True
        idv+=1
        ids[s]=low[s]=idv
        while stk:
            at,parent,idx=stk.pop()
            if idx<len(adj[at]):
                to=adj[at][idx]
                stk.append((at,parent,idx+1))
                if to==parent:
                    continue
                if not visited[to]:
                    visited[to]=True
                    idv+=1
                    ids[to]=low[to]=idv
                    stk.append((to,at,0))
                else:
                    low[at]=min(low[at],ids[to])
            else:
                if parent!=-1:
                    low[parent]=min(low[parent],low[at])
                    if ids[parent]<low[at]:
                        bridges.add((min(parent,at),max(parent,at)))
    return bridges
brid=bridge()
print(len(brid))
brid=sorted(brid)
if len(brid)>0:
    for a,b in brid:
        print(a+1,b+1)