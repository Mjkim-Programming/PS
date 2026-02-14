import sys
from functools import cmp_to_key
input=sys.stdin.readline
def cmp(a,b):
    f,s=str(a)+str(b),str(b)+str(a)
    if f>s:
        return -1
    elif f<s:
        return 1
    else:
        return 0
k,n=map(int,input().split())
arr=[int(input()) for _ in range(k)]
arr2=arr[:]
arr.sort(key=cmp_to_key(cmp))
arr2.sort(reverse=True)
used=False
res=""
for i in range(k):
    if arr2[0]==arr[i] and not used:
        for j in range(n-k+1):
            res+=str(arr[i])
        used=True
    else:
        res+=str(arr[i])
print(res)