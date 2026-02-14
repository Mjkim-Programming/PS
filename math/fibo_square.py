import sys
input=sys.stdin.readline
def matmul(A,B,m):
    a,b=A[0];c,d=A[1];e,f=B[0];g,h=B[1]
    return [
        [(a*e+b*g)%m, (a*f+b*h)%m],
        [(c*e+d*g)%m, (c*f+d*h)%m]
    ]
def matpow(A,e,m):
    res=[[1,0],[0,1]]
    base=A
    while e>0:
        if e&1:
            res=matmul(res,base,m)
        base=matmul(base,base,m)
        e>>=1
    return res
base=[[1,1],[1,0]]
n=int(input())
m=1_000_000_007
res=matpow(base,n,m)
print((res[0][0]*res[0][1])%m)