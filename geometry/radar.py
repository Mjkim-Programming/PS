import sys
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def ccw(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
def allcoll(pts):
    if len(pts)<=2:
        return True
    a=pts[0]
    b=pts[1]
    for i in range(2,len(pts)):
        if ccw(a,b,pts[i])!=0:
            return False
    return True
def dist2(a,b):
    dx=a.x-b.x
    dy=a.y-b.y
    return dx*dx + dy*dy
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
t=int(input())
for tc in range(1,t+1):
    a,b,c=Point(0,0),Point(0,0),Point(0,0)
    a.x,a.y,b.x,b.y,c.x,c.y=map(int,input().split())
    ab2,bc2,ac2=dist2(a,b),dist2(b,c),dist2(a,c)
    arr=[(ab2,a,b,c),(bc2,b,c,a),(ac2,a,c,b)]
    longest=max(arr,key=lambda x: x[0])
    total=ab2+bc2+ac2
    if longest[0]>=total-longest[0]:
        p,q=longest[1],longest[2]
        cent=midpoint(p,q)
    else:
        cent=circumcenter(a,b,c)
    print(f"Case #{tc}: {cent.x:.2f} {cent.y:.2f}")