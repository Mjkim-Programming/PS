import sys
input=sys.stdin.readline
n=int(input())
arr=sorted(list(map(int,input().split())))
l,r=0,n-1
mv,minv=10**18,(l,r)
while l<r:
    if abs(arr[l]+arr[r])<abs(mv):
        mv=arr[l]+arr[r]
        minv=(l,r)
    if arr[l]+arr[r]<0:
        l+=1
    elif arr[l]+arr[r]>0:
        r-=1
    elif arr[l]+arr[r]==0:
        l+=1
print(arr[minv[0]],arr[minv[1]])