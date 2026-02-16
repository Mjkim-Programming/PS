import sys
input=sys.stdin.readline
n=int(input())
arr=list(input().rstrip())
INF=10**9
dp=[INF]*(n)
dp[0]=0
prev={"B":"J","O":"B","J":"O"}
for i in range(1,n):
    p=prev[arr[i]]
    for j in range(i):
        if arr[j]==p:
            dp[i]=min(dp[i],dp[j]+(j-i)**2)
print(-1 if dp[-1]==INF else dp[-1])
