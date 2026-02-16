import sys
input=sys.stdin.readline
t=int(input())
def f(x):
    return x**2 + 1
for _ in range(t):
    n=int(input())
    res=f(n)
    if n>=3:
        res+=f(n-2)-1
    print(res)