import heapq
import sys
input=sys.stdin.readline
INF=float('INF')
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d,=map(int,input().split())
        adj[u].append((v,c,d))
    dp=[[INF]*(n+1) for _ in range(m+1)]
    dp[0][1]=0
    for c in range(m+1):
        for u in range(1,n+1):
            if dp[c][u]==INF:
                continue
            cur=dp[c][u]
            for v,cost,t in adj[u]:
                nc=c+cost
                if nc<=m:
                    dp[nc][v]=min(dp[nc][v],cur+t)
    ans=min(dp[c][n] for c in range(m+1))
    print("Poor KCM" if ans == INF else ans)