import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().rstrip().split()))
dp={}
for v in arr:
    if v-1 in dp:
        dp[v]=dp[v-1]+1
    else:
        dp[v]=1
print(max(list(dp.values())))
