import sys
from functools import cmp_to_key
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def area(pts):
    res,n=0,len(pts)
    for i in range(n):
        ni=(i+1)%n
        res+=pts[i].x*pts[ni].y
        res-=pts[i].y*pts[ni].x
    return 0.5*abs(res)
t=int(input())
res=0
for _ in range(t):
    n=int(input())
    pts=[]
    for _ in range(n):
        a,b=map(int,input().split())
        pts.append(Point(a,b))
    res+=area(pts)
print(int(res))