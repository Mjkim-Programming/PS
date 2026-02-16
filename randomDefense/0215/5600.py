import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
n=int(input())
parts=[2]*(a+b+c+1)
tests=[]
for _ in range(n):
    i,j,k,r=map(int,input().split())
    tests.append((i,j,k,r))
for i,j,k,r in tests:
    if r==1:
        parts[i],parts[j],parts[k]=1,1,1
changed=True
while changed:
    changed=False
    for i,j,k,r in tests:
        if r==0:
            arr=[parts[i],parts[j],parts[k]]
            idx=[i,j,k]
            if arr.count(1)==2:
                for m in range(3):
                    if arr[m]!=1 and parts[idx[m]]!=0:
                        parts[idx[m]]=0
                        changed=True
for i in range(1,len(parts)):
    print(parts[i])