from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
indeg = [0]*(N+1)
for _ in range(M):
    arr = list(map(int, input().split()))
    K = arr[0]
    arr = arr[1:]
    for i in range(K):
        if i + 1 < K:
            adj[arr[i]].append(arr[i+1])
            indeg[arr[i+1]] += 1
visited = 0
q = deque()
order = []
for u in range(1, N+1):
    if indeg[u] == 0:
        q.append(u)
while q:
    u = q.popleft()
    order.append(u)
    visited += 1
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
if visited != N:
    print(0)
else:
    print(*order, sep="\n")