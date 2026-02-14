import sys
input=sys.stdin.readline
n,t=map(int,input().split())
pts=[]
class Point:
    def __init__(self,s,x,y):
        self.s=s
        self.x=x
        self.y=y
for _ in range(n):
    s,x,y=map(int,input().split())
    pts.append(Point(s,x,y))
INF=10**18
dist=[[INF]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        d=abs(pts[i].x-pts[j].x)+abs(pts[i].y-pts[j].y)
        if pts[i].s == 1 and pts[j].s == 1:
            dist[i][j]=min(t,d)
            dist[j][i]=min(t,d)
        else:
            dist[i][j]=d
            dist[j][i]=d
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
m=int(input())
for _ in range(m):
    qx,qy=map(int,input().split())
    print(dist[qy-1][qx-1])