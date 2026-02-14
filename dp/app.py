import sys
input=sys.stdin.readline
n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
max_cost = sum(cost)
dp = [0]*(max_cost+1)
for i in range(n):
    c = cost[i]; memory = mem[i]
    for j in range(max_cost, c-1, -1):
        dp[j] = max(dp[j], dp[j-c]+memory)
for i in range(max_cost+1):
    if dp[i] >= m:
        print(i)
        break