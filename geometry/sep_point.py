import sys
from functools import cmp_to_key
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def ccw(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
def dist2(a,b):
    dx=a.x-b.x
    dy=a.y-b.y
    return dx*dx + dy*dy
def cmpConvhull(a,b):
    if a.x==b.x:
        if a.y<b.y:
            return -1
        else:
            return 1
    if a.x<b.x:
        return -1
    else:
        return 1
def convhull(pts):
    if len(pts)<=1:
        return pts[:]
    points=sorted(pts, key=cmp_to_key(cmpConvhull))
    hull=[]
    for p in points:
        while len(hull)>=2 and ccw(hull[len(hull)-2],hull[-1],p) <= 0:
            hull.pop()
        hull.append(p)
    t=len(hull)+1
    for i in range(len(points)-2,-1,-1):
        p=points[i]
        while len(hull)>=t and ccw(hull[len(hull)-2],hull[-1],p) <= 0:
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull
def pointConvex(hull,P):
    n=len(hull)
    if n==1:
        return hull[0].x==P.x and hull[0].y==P.y
    if n==2:
        return ccw(hull[0],hull[1],P)==0 and onseg(hull[0],hull[1],P)
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
def onseg(a,b,c):
    return min(a.x,b.x)<=c.x<=max(a.x,b.x) and min(a.y,b.y)<=c.y<=max(a.y,b.y)
def seginter(a,b,c,d):
    ab1=ccw(a,b,c)
    ab2=ccw(a,b,d)
    cd1=ccw(c,d,a)
    cd2=ccw(c,d,b)
    if ab1==0 and onseg(a,b,c): return True
    if ab2==0 and onseg(a,b,d): return True
    if cd1==0 and onseg(c,d,a): return True
    if cd2==0 and onseg(c,d,b): return True
    return ab1*ab2<0 and cd1*cd2<0
def hullinter(h1,h2):
    n=len(h1)
    m=len(h2)
    for i in range(n):
        a=h1[i]
        b=h1[(i+1)%n]
        for j in range(m):
            c=h2[j]
            d=h2[(j+1)%m]
            if seginter(a,b,c,d):
                return True
    return False
def allcoll(pts):
    if len(pts)<=2:
        return True
    a=pts[0]
    b=pts[1]
    for i in range(2,len(pts)):
        if ccw(a,b,pts[i])!=0:
            return False
    return True
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    black,white=[],[]
    for _ in range(n):
        a,b=map(int,input().split())
        black.append(Point(a,b))
    for _ in range(m):
        a,b=map(int,input().split())
        white.append(Point(a,b))
    bhull,whull=convhull(black),convhull(white)
    if allcoll(bhull+whull):
        pts=bhull+whull
        a=pts[0]
        b=pts[1]
        usex=abs(a.x-b.x)>=abs(a.y-b.y)
        if usex:
            bmin=min(p.x for p in black)
            bmax=max(p.x for p in black)
            wmin=min(p.x for p in white)
            wmax=max(p.x for p in white)
        else:
            bmin=min(p.y for p in black)
            bmax=max(p.y for p in black)
            wmin=min(p.y for p in white)
            wmax=max(p.y for p in white)
        if bmax<wmin or wmax<bmin:
            print("YES")
        else:
            print("NO")
    else:
        if hullinter(bhull,whull):
            print("NO")
            continue
        for p in bhull:
            if pointConvex(whull,p):
                print("NO")
                break
        else:
            for p in whull:
                if pointConvex(bhull,p):
                    print("NO")
                    break
            else:
                print("YES")