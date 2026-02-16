import sys
from math import gcd
input=sys.stdin.readline
t=int(input())
for tc in range(1,t+1):
    m={}
    n=int(input())
    pts=[tuple(map(int,input().split())) for _ in range(n)]
    res=1
    for i in range(n):
        slopes={}
        x1,y1=pts[0]
        lmax=0
        for j in range(i+1,n):
            x2,y2=pts[j]
            dx=x2-x1
            dy=y2-y1
            g=gcd(dx,dy)
            dx//=g
            dy//=g
            if dx<0:
                dx=-dx
                dy=-dy
            elif dx==0:
                dy=1
            elif dy==0:
                dx=1
            slopes[(dx,dy)]=slopes.get((dx,dy),0)+1
            lmax=max(lmax,slopes[(dx,dy)])
        res=max(res,lmax+1)
    print(f"Case #{tc}: {res}")