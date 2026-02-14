T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    adj = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        adj[a][b] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(x, y):
        if (x < 0 or x >= M or y < 0 or y >= N):
            return
        if adj[x][y] == 0:
            return
        adj[x][y] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])

    res = 0
    for i in range(M):
        for j in range(N):
            if adj[i][j] == 1:
                dfs(i, j)
                res += 1

    print(res)