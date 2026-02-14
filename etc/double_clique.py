import sys
input=sys.stdin.readline
n,m=map(int,input().split())
deg=[0]*n
mo=10**9 + 7
for _ in range(m):
    u,v=map(int,input().split())
    u-=1;v-=1
    deg[u]+=1
    deg[v]+=1
deg.sort(reverse=True)
siz,s=-1,0
for i in range(n):
    s+=deg[i]
    left=s-(i+1)*i
    if left==2*m-s:
        siz=i+1
        break
if siz==-1:
    print(0)
    sys.exit(0)
freq=[0]*(max(deg)+1)
for i in deg:
    freq[i]+=1
ans=1
for i in range(siz):
    if deg[i]==siz-1:
        ans+=1
freq_C=0
for i in range(siz):
    if deg[i]==siz:
        freq_C+=1
for i in range(siz,n):
    if deg[i]==siz:
        ans+=1+freq_C
        ans%=mo
print(ans)