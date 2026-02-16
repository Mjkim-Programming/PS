import sys
from math import gcd
input=sys.stdin.readline
n,d=int(input()),{}
for _ in range(n):
    x,y=map(int,input().split())
    g=gcd(abs(x),abs(y))
    x//=g
    y//=g
    if d.get((x,y)) != None:
        d[(x,y)]+=1
    else:
        d[(x,y)]=1
print(max(d.values()))