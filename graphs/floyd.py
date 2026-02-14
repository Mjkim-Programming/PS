import sys
input=sys.stdin.readline
n,m=int(input()),int(input())
INF=float('INF')
adj=[[INF]*(n) for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    adj[a][b]=min(adj[a][b],c)
for i in range(n):
    adj[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
for a in adj:
    for v in a:
        if v==INF:
            print(0,end=' ')
        else:
            print(v,end=' ')
    print()