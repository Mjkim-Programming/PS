import sys
sys.setrecursionlimit(5000)

N = int(input())
adj = []
adj_cb = []
cnt = 0

for _ in range(N):
    inp = input()
    adj.append(list(inp.strip()))
    adj_cb.append(list(inp.replace("G", "R").strip()))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs_cb(x, y, o):
    global cnt
    if (x < 0 or x >= N or y < 0 or y >= N):
        return
    if adj_cb[x][y] != o:
        return
    cnt += 1
    adj_cb[x][y] = 0
    for i in range(4):
        dfs_cb(x+dx[i], y+dy[i], o)
        
def dfs(x, y, o):
    global cnt
    if (x < 0 or x >= N or y < 0 or y >= N):
        return
    if adj[x][y] != o:
        return
    cnt += 1
    adj[x][y] = 0
    for i in range(4):
        dfs(x+dx[i], y+dy[i], o)

cb_res = 0
for i in range(N):
    for j in range(N):
        if adj_cb[i][j] != 0:
            dfs_cb(i, j, adj_cb[i][j])
            cb_res += 1
            cnt = 0

res = 0
for i in range(N):
    for j in range(N):
        if adj[i][j] != 0:
            dfs(i, j, adj[i][j])
            res += 1
            cnt = 0

print(res, cb_res)