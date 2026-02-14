import math
import random
import sys
input=sys.stdin.readline
def get_d(n):
    r,s=n,0
    while r % 2 == 0:
        r //=2
        s+=1
    return r,s
def miller_rabin(n):
    a_s=[2,325,9375,28178,450775,9780504,1795265022]
    if n==1:
        return False
    if n in (2,3):
        return True
    if n%2==0:
        return False
    d,s=get_d(n-1)
    for a in a_s:
        if a>=n:
            continue
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for _ in range(s-1):
            x=pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True
def pollard_rho(n):
    if n%2==0:
        return 2
    if miller_rabin(n):
        return n
    while True:
        x=random.randrange(2,n-1)
        y=x
        c=random.randrange(2,n-1)
        d=1
        while d==1:
            x,y=(x*x+c)%n,(y*y+c)%n
            y=(y*y+c)%n
            d=math.gcd(abs(x-y),n)
        if d != n:
            return d
def factor(n,res):
    if n==1:
        return
    if miller_rabin(n):
        res.append(n)
    else:
        d=pollard_rho(n)
        factor(d,res)
        factor(n//d,res)
n=int(input())
if n==1:
    print(1)
    sys.exit(0)
fts=[];factor(n,fts);fts.sort()
res,prev,cnt=1,fts[0],1
for v in fts[1:]:
    if v==prev:
        cnt+=1
    else:
        res*=(cnt+1)
        prev=v
        cnt=1
res*=(cnt+1)
print(res)