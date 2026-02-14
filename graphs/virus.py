V, E = int(input()), int(input())
adj = [[] for _ in range(V)]
visited = [False] * V
cnt = 0

for _ in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

def dfs(at):
    global cnt
    if visited[at]:
        return
    visited[at] = True
    cnt += 1
    neighbor = adj[at]
    for nxt in neighbor:
        dfs(nxt)

dfs(0)
print(cnt - 1)