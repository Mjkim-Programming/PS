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
    return res
n=int(input())
for _ in range(n):
    s=input().strip()
    pts=[]
    x,y=0,0
    pts.append(Point(x,y))
    for c in s:
        if c=='N':
            y+=1
        elif c=='S':
            y-=1
        elif c=='E':
            x+=1
        else:
            x-=1
        pts.append(Point(x,y))
    a=area(pts)
    print("CCW" if a>0 else "CW")