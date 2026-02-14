import math
import sys
input=sys.stdin.readline
v,n=map(float,input().split())
n=int(n)
def simpson(a,b,l,r,n):
    dx=(r-l)/n
    def g(x):
        y=a*math.exp(-x*x)+b*math.sqrt(x)
        return y*y
    s=g(l)+g(r)
    for i in range(1,n):
        x=l+dx*i
        s+=4*g(x) if i&1 else 2*g(x)
    return s*dx/3.0
def vol(a,b,h):
    p=[
        0.0,
        h*0.02,
        h*0.08,
        h*0.25,
        h*0.6,
        h
    ]
    n=4000
    res=0.0
    for i in range(5):
        res += simpson(a,b,p[i],p[i+1],n)
    return math.pi*res
idx,bdiff=0,float('INF')
for i in range(n):
    a,b,h=map(float,input().split())
    V=vol(a,b,h)
    diff=abs(V-v)
    if diff<bdiff:
        bdiff,idx=diff,i
print(idx)