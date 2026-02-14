import sys
input=sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n)]

for _ in range(m):
    alp, bet = map(int, input().split())
    adj[alp-1].append(bet-1)
    adj[bet-1].append(alp-1)
    
depth = 0
stk = [(a-1, depth)]
visited = [False] * n
while stk:
    x, dep = stk.pop()
    if x == b-1:
        print(dep)
        exit()
    if visited[x]:
        continue
    visited[x] = True
    for nxt in adj[x]:
        if not visited[nxt]:
            stk.append((nxt, dep + 1))
print(-1)