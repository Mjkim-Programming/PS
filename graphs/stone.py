import sys
from collections import deque
input=sys.stdin.readline
a,b,n,m=map(int,input().split())
def getavail(x,a,b):
    vals=[x+1,x-1,x+a,x-a,x+b,x-b,a*x,b*x]
    res=[]
    for v in vals:
        if 0<=v<=100000:
            res.append(v)
    return res
visited=[False]*100001
visited[n]=True
deq=deque([(n,0)])
res=0
while deq:
    x,depth=deq.popleft()
    if x==m:
        res=depth
        break
    for v in getavail(x,a,b):
        if not visited[v]:
            visited[v]=True
            deq.append((v,depth+1))
print(res)
