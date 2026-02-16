import sys
import math
input=sys.stdin.readline
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
def cross(a,b):
    return a.x*b.y-a.y*b.x
def dot(a,b):
    return a.x*b.x+a.y*b.y
t=int(input())
for _ in range(t):
    n=int(input())
    targets=[]
    for _ in range(n):
        a,b,c,d=map(int,input().split())
        targets.append((Point(a,b),Point(c,d)))
    total=0
    for target in targets:
        a,b=target
        theta=math.atan2(abs(cross(a,b)),dot(a,b))
        total+=theta
    exp=total/(2*math.pi)
    print(f"{exp:.5f}")