import heapq
import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    x=int(input())
    heapq.heappush(arr,x)
while len(arr)!=1:
    x,y=heapq.heappop(arr),heapq.heappop(arr)
    heapq.heappush(arr,x+y)
print(arr[0])