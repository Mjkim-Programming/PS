import math
import sys
input=sys.stdin.readline
def phi(x):
    res,y,d=x,x,2
    while d*d<=y:
        if y%d==0:
            res=res//d*(d-1)
            while y%d==0:
                y//=d
        d+=1
    if y>1:
        res=res//y*(y-1)
    return res
def div(x):
    res=[]
    for d in range(1,int(math.isqrt(x))+1):
        if n%d==0:
            res.append(d)
            if d*d!=n:
                res.append(n//d)
    return res
n=int(input())
if n==1:
    print(1)
    sys.exit(0)
if n%2==1:
    print(-1)
    sys.exit(0)
ans=-1
divs=div(n)
divs.sort()
for d in divs:
    if d*phi(d)==n:
        print(d)
        sys.exit(0)
print(-1)