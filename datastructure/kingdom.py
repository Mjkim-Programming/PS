import sys
input=sys.stdin.readline
MAXN=500
n,m=map(int,input().split())
parent=[i for i in range(n)]
def find(x):
    if x==parent[x]:
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    parent[y]=x
def stp(x):
    return x.replace("Kingdom of ","")
d={}
revd={}
idx=0
for _ in range(n):
    inp=input().rstrip()
    d[stp(inp)]=idx
    revd[idx]=stp(inp)
    idx+=1
for _ in range(m):
    a,b,res=input().split(",")
    a,b=a.strip(),b.strip()
    res=int(res)
    a,b=stp(a),stp(b)
    if res==1:
        union(d[a],d[b])
    else:
        union(d[b],d[a])
s=set()
for i in range(n):
    s.add(find(i))
print(len(s))
arr=sorted([revd[v] for v in s])
for v in arr:
    print(f"Kingdom of {v}")