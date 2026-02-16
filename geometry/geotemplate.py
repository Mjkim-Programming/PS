import sys
from functools import cmp_to_key
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def ccw(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
def sortpts(pts,clockwise):
    points=sorted(pts,key=lambda p: (p.y, p.x))
    pivot=points[0]
    def cmpsortpts(a,b):
        v=ccw(pivot,a,b)
        if clockwise:
            if v>0:
                return -1
            if v<0:
                return 1
        else:
            if v>0:
                return 1
            if v<0:
                return -1
        da=(a.x-pivot.x)**2+(a.y-pivot.y)**2
        db=(b.x-pivot.x)**2+(b.y-pivot.y)**2
        return da-db
    pts=[pivot]+sorted(pts[1:],key=cmp_to_key(cmpsortpts))
def orientation(a,b,c):
    v = ccw(a,b,c)
    return v
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
def calipers(hull):
    n=len(hull)
    if n<2: return 0
    if n==2: return dist2(hull[0],hull[1])
    max_d2,j=0,1
    for i in range(n):
        ni=(i+1)%n
        while True:
            nj=(j+1)%n
            if ccw(hull[i],hull[ni],hull[nj])>ccw(hull[i],hull[ni],hull[j]):
                j=nj
            else:
                break
        max_d2=max([max_d2,dist2(hull[i],hull[j]),dist2(hull[ni],hull[j])])
    return max_d2
def calipers_pair(hull):
    n=len(hull)
    if n==2: return (hull[0],hull[1])
    max_d2,farthest,j=0,(None,None),1
    for i in range(n):
        ni=(i+1)%n
        while True:
            nj=(j+1)%n
            if ccw(hull[i],hull[ni],hull[nj])>ccw(hull[i],hull[ni],hull[j]):
                j=nj
            else:
                break
        d2_i=dist2(hull[i],hull[j])
        d2_ni=dist2(hull[ni],hull[j])
        if d2_i>max_d2:
            max_d2=d2_i
            farthest=(hull[i],hull[j])
        if d2_ni>max_d2:
            max_d2=d2_ni
            farthest=(hull[ni],hull[j])
    return farthest
def area(pts):
    res,n=0,len(pts)
    for i in range(n):
        ni=(i+1)%n
        res+=pts[i].x*pts[ni].y
        res-=pts[i].y*pts[ni].x
    return 0.5*res
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
def cross(a,b):
    return a.x*b.y-a.y*b.x
def dot(a,b):
    return a.x*b.x+a.y*b.y
def midpoint(a,b):
    return Point((a.x+b.x)/2,(a.y+b.y)/2)
def circumcenter(a,b,c):
    d=2*(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y))
    ux=((a.x*a.x+a.y*a.y)*(b.y-c.y)+
        (b.x*b.x+b.y*b.y)*(c.y-a.y)+
        (c.x*c.x+c.y*c.y)*(a.y-b.y)) / d
    uy=((a.x*a.x+a.y*a.y)*(c.x-b.x)+
        (b.x*b.x+b.y*b.y)*(a.x-c.x)+
        (c.x*c.x+c.y*c.y)*(b.x-a.x)) / d
    return Point(ux,uy)