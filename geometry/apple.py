import sys
from functools import cmp_to_key
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def ccw(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
def area(pts):
    res,n=0,len(pts)
    for i in range(n):
        ni=(i+1)%n
        res+=pts[i].x*pts[ni].y
        res-=pts[i].y*pts[ni].x
    return 0.5*abs(res)
def pointConvex(hull,P):
    n=len(hull)
    prev=0
    for i in range(n):
        a=hull[i]
        b=hull[(i+1)%n]
        v=ccw(a,b,P)
        if v!=0:
            if prev==0:
                prev=1 if v>0 else -1
            elif (v>0 and prev<0) or (v<0 and prev>0):
                return False
    return True
hull=[]
for i in range(3):
    a,b=map(int,input().split())
    hull.append(Point(a,b))
print(f"{area(hull):.1f}")
n=int(input())
apples=[]
for i in range(n):
    a,b=map(int,input().split())
    apples.append(Point(a,b))
cnt=0
for apple in apples:
    if pointConvex(hull,apple):
        cnt+=1
print(cnt)