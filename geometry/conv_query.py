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
def pointInPolygon(hull,P):
    n=len(hull)
    if n<3: return pointConvex(hull,P)
    if ccw(hull[0],hull[1],P)<0 or ccw(hull[0],hull[n-1],P)>0: return False
    l,r=1,n-1
    while l+1<r:
        m=(l+r)//2
        if ccw(hull[0],hull[m],P)>=0: l=m
        else: r=m
    return ccw(hull[l],hull[r],P)>=0
def prv(i,n):
    return n-1 if i==0 else i-1
def nxt(i,n):
    return 0 if i+1==n else i+1
def isLeftTangent(P, Q, i):
    n=len(P)
    ip,iq=prv(i,n),nxt(i,n)
    return ccw(Q,P[i],P[ip]) != 1 and ccw(Q,P[i],P[iq]) == -1
def isRightTangent(P, Q, i):
    n=len(P)
    ip,iq=prv(i,n),nxt(i,n)
    return ccw(Q,P[i],P[ip]) != 1 and ccw(Q,P[i],P[iq]) == 1
def findLeftTangent(P,Q):
    n=len(P)
    l,r=0,n
    while l<r:
        m=(l+r)>>1
        if isLeftTangent(P,Q,m): return m
        o1=ccw(Q,P[m],P[nxt(m,n)])
        o2=ccw(Q,P[0],P[1])
        if o1>o2: l=m+1
        else: r=m
    return l%n
def findRightTangent(P,Q):
    n=len(P)
    l,r=0,n
    while l<r:
        m=(l+r)>>1
        if isRightTangent(P,Q,m): return m
        o1=ccw(Q,P[m],P[nxt(m,n)])
        o2=ccw(Q,P[0],P[1])
        if o1<o2: l=m+1
        else: r=m
    return l%n
def getTangent(P,Q):
    L=findLeftTangent(P,Q)
    R=findRightTangent(P,Q)
    return (L,R)
def isCovered(P,Qi,Qj,Li,Rj):
    return ccw(P[Rj],Qj,Qi)>=0 and ccw(Qj,P[Li],Qi)>=0
def getArcUnion(R1,L1,R2,L2,n):
    def get_intervals(R,L,n):
        if (R+1)%n == L: return []
        res=[]
        s,e=(R+1)%n,(L-1+n)%n
        if s<=e: res.append((s,e))
        else:
            res.append((s,n-1))
            res.append((0,e))
        return res
    intervals=sorted(get_intervals(R1,L1,n)+get_intervals(R2,L2,n))
    if not intervals: return 0
    total_rem=0
    cur_s,cur_e=intervals[0]
    for i in range(1,len(intervals)):
        ns,ne=intervals[i]
        if ns<=cur_e+1:
            cur_e=max(cur_e,ne)
        else:
            total_rem+=(cur_e-cur_s+1)
            cur_s,cur_e=ns,ne
    total_rem+=(cur_e-cur_s+1)
    return total_rem
n,m,k=map(int,input().split())
P,Q=[],[]
for _ in range(n):
    a,b=map(int,input().split())
    P.append(Point(a,b))
for _ in range(m):
    a,b=map(int,input().split())
    Q.append(Point(a,b))
QinHull=[False]*m
tangents=[None]*m
for i in range(m):
    QinHull[i]=pointInPolygon(P,Q[i])
    if not QinHull[i]:
        tangents[i]=getTangent(P,Q[i])
for _ in range(k):
    i,j=map(int,input().split())
    i-=1
    j-=1
    if QinHull[i] and QinHull[j]:
        print(n)
    elif QinHull[i] or QinHull[j]:
        oidx=j if QinHull[i] else i
        L,R=tangents[oidx]
        rem=(L-R+n)%n-1
        if (L-R+n)%n==0: rem=-1
        print(n-max(0,rem)+1)
    else:
        Li,Ri=tangents[i]
        Lj,Rj=tangents[j]
        if isCovered(P,Q[i],Q[j],Lj,Rj):
            rem=(Lj-Rj+n)%n-1
            print(n-max(0,rem)+1)
        elif isCovered(P,Q[j],Q[i],Li,Ri):
            rem=(Li-Ri+n)%n-1
            print(n-max(0,rem)+1)
        else:
            union=getArcUnion(Ri,Li,Rj,Lj,n)
            print(n-union+2)
        continue