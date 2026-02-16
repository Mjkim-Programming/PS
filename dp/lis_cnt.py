import sys
input=sys.stdin.readline
m=998244353
n=int(input())
arr=list(map(int,input().rstrip().split()))
dp=[1]*n
for i in range(1,n):
    total=1
    for j in range(i):
        if arr[j]<arr[i]:
            total=(total+dp[j])%m
    dp[i]=total
print(*dp)
