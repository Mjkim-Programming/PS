import sys
input=sys.stdin.readline
MAXN=4_000_000
def seive():
    a,p=[i for i in range(0, MAXN+1)],[]
    for i in range(2,MAXN+1):
        if a[i]==0: continue
        for j in range(2*i,MAXN+1,i):
            a[j]=0
    for i in range(2,MAXN+1):
        if a[i]!=0: p.append(i)
    return p
primes=seive()
m=len(primes)
l,r,c,ans=0,0,0,0
n=int(input())
while True:
    if c<n:
        if r==m:
            break
        c+=primes[r]
        r+=1
    else:
        c-=primes[l]
        l+=1
    if c==n:
        ans+=1
print(ans)