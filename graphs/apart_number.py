N = int(input())
adj = []
cnt = 0

for _ in range(N):
    adj.append(list(map(int, input().strip())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    if (x < 0 or x >= N or y < 0 or y >= N):
        return
    if adj[x][y] == 0:
        return
    cnt += 1
    adj[x][y] = 0
    for i in range(4):
        dfs(x+dx[i], y+dy[i])

res = 0
out = []
for i in range(N):
    for j in range(N):
        if adj[i][j] == 1:
            dfs(i, j)
            out.append(cnt)
            res += 1
            cnt = 0

print(res)
print(*sorted(out), sep="\n")