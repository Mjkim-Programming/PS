import sys
input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
trig=[1]
idx=1
while trig[-1]<=n:
    idx+=1
    trig.append(trig[-1]+(idx)*(idx+1)//2)
for i in range(1,n+1):
    arr=[i]
    for v in trig:
        if v>i:
            break
        arr.append(dp[i-v])
    dp[i]=min(arr)+1
print(dp[n])
