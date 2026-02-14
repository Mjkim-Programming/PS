import math
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    arr=list(input().split())
    n,arr=int(arr[0]),arr[1:]
    parts=0
    for v in arr:
        parts+=int(v[1:])
    buffalo=parts//7
    sheep=parts%7
    trb,trs=math.ceil(buffalo/3),math.ceil(sheep/6)
    print(trb+trs)