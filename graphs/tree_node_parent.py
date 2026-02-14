import sys
input=sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

parent = [-1] * N
stk = [0]
parent[0] = 0

while stk:
    u = stk.pop()
    for v in adj[u]:
        if parent[v] == -1:
            parent[v] = u
            stk.append(v)

for i in range(1, N):
    print(parent[i] + 1)