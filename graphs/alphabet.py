R, C = map(int, input().split())
adj = [list(input().strip()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

maxDepth = 0
def dfs(x, y, depth, mask):
    global maxDepth
    maxDepth = max(maxDepth, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= C or ny < 0 or ny >= R):
            continue
        idx = ord(adj[ny][nx]) - ord('A')
        if mask & (1 << idx):
            continue
        dfs(nx, ny, depth + 1, mask | (1 << idx))
    

dfs(0, 0, 1, 1 << (ord(adj[0][0]) - ord('A')))
print(maxDepth)