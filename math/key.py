import math
import random
import sys
input=sys.stdin.readline
def get_d(n):
    r,s=n,0
    while r % 2 == 0:
        r //=2
        s+=1
    return r,s
def miller_rabin(n):
    a_s=[2,325,9375,28178,450775,9780504,1795265022]
    if n==1:
        return False
    if n in (2,3):
        return True
    if n%2==0:
        return False
    d,s=get_d(n-1)
    for a in a_s:
        if a>=n:
            continue
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for _ in range(s-1):
            x=pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True
a,b=map(int,input().split())
for i in range(a,b+1):
    if i==9:
        print(i,end=' ')
    if miller_rabin(i):
        print(i,end=' ')