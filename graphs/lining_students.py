from collections import deque
import sys
input=sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
indeg = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    indeg[b] += 1
q = deque()
for i in range(N):
    if indeg[i] == 0:
        q.append(i)
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
print(*[x+1 for x in order])