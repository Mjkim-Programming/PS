import sys
input=sys.stdin.readline
m=int(input())
deg=[0]*m
for i in range(m):
    arr=list(map(int,input().split()))
    deg[i]+=len(arr)-1
deg.sort(reverse=True)
siz,s=-1,0
tdeg=sum(deg)
for i in range(m):
    s+=deg[i]
    left=s-(i+1)*i
    if left==tdeg-s:
        siz=i+1
        break
if siz==-1:
    print(0)
    sys.exit(0)
freq=[0]*(max(deg)+1)
for i in deg:
    freq[i]+=1
ans=1 if 1 <= siz <= m-1 else 0
if siz-1>=1:
    for i in range(siz):
        if deg[i]==siz-1:
            ans+=1
freq_C=0
for i in range(siz):
    if deg[i]==siz:
        freq_C+=1
for i in range(siz,m):
    if deg[i]==siz:
        if siz+1<=m-1:
            ans+=1
        if 1<=siz<=m-1:
            ans+=freq_C
print(ans)