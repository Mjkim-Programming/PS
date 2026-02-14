import sys
input=sys.stdin.readline

def solve():
    n,c=map(int,input().split())
    arr=list(input().strip())
    cost=list(map(int,input().split()))
    pairs=[]
    for i in range(n//2):
        j=n-i-1
        if arr[i] != arr[j]:
            pairs.append((i,j,cost[i],cost[j]))
    if len(pairs)==0:
        print(0)
        return
    minL,minR,_,_=pairs[0]
    prefix=[]
    

t=int(input())
for _ in range(t):
    solve()