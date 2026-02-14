from collections import deque
import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    indeg = [0]*N
    for _ in range(K):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        indeg[v] += 1
    W = int(input()) - 1
    q = deque()
    order = []
    for i in range(N):
        if indeg[i] == 0:
            q.append(i)
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    dp = [0]*N
    for u in order:
        dp[u] += D[u]
        for v in adj[u]:
            if dp[v] < dp[u]:
                dp[v] = dp[u]
    
    print(dp[W])