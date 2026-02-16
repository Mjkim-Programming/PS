import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=input().rstrip()
cnt=0
for ch in arr:
    if ch=='0':
        cnt+=1
        if cnt>=k:
            print(0)
            sys.exit(0)
    else:
        cnt=0
print(1)