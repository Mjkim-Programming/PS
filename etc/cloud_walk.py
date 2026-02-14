import sys
input=sys.stdin.readline
def to_complete(adj):
    adj2=[l[:] for l in adj]
    n=len(adj2)
    needed=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if j not in adj2[i]:
                adj2[i].append(j)
                adj2[j].append(i)
                needed.append((min(i,j),max(i,j)))
    return needed
n=int(input())
adj=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    adj[u].append(v)
    adj[v].append(u)
if n==2:
    print(0)
    print(1)
    sys.exit(0)
if n==3 or n==4:
    need=to_complete(adj)
    print(len(need))
    print(1)
    if len(need)!=0:
        for u,v in need:
            print(u+1, v+1)
    sys.exit(0)
needed=[]
for i in range(n):
    if i==0:
        continue
    if i not in adj[0]:
        adj[0].append(i)
        adj[i].append(0)
        needed.append((min(0,i),max(0,i)))
print(len(needed))
print(2)
if len(needed)!=0:
    for u,v in needed:
        print(u+1,v+1)