import math
import sys
from functools import cmp_to_key
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def dist2(a,b):
    dx=a.x-b.x
    dy=a.y-b.y
    return dx*dx + dy*dy
n,q=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
right=[]
for i in range(n-1):
    if y[i]<y[i+1]:
        right.append(3*math.sqrt(dist2(Point(x[i],y[i]),Point(x[i+1],y[i+1]))))
    elif y[i]==y[i+1]:
        right.append(2*math.sqrt(dist2(Point(x[i],y[i]),Point(x[i+1],y[i+1]))))
    else:
        right.append(math.sqrt(dist2(Point(x[i],y[i]),Point(x[i+1],y[i+1]))))
left=[0]*n
for i in range(n-1,0,-1):
    if y[i]<y[i-1]:
        left[i]=3*math.sqrt(dist2(Point(x[i],y[i]),Point(x[i-1],y[i-1])))
    elif y[i]==y[i-1]:
        left[i]=2*math.sqrt(dist2(Point(x[i],y[i]),Point(x[i-1],y[i-1])))
    else:
        left[i]=math.sqrt(dist2(Point(x[i],y[i]),Point(x[i-1],y[i-1])))
prefixL,prefixR=[0]*n,[0]*n
for i in range(1,n):
    prefixR[i]=prefixR[i-1]+right[i-1]
for i in range(n-2,-1,-1):
    prefixL[i]=prefixL[i+1]+left[i+1]
for _ in range(q):
    i,j=map(int,input().split())
    i-=1
    j-=1
    print(prefixR[j]-prefixR[i] if i<j else prefixL[j]-prefixL[i])