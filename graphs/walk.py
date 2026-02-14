import sys
input=sys.stdin.readline
M=1_000_000_007
def matmul(A,B):
    n=len(A)
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                c[i][j] = (c[i][j]+A[i][k]*B[k][j])%M
    return c
def matpow(A,e):
    if e == 1:
        return A
    h=matpow(A,e//2)
    h2=matmul(h,h)
    if e % 2 == 0:
        return h2
    else:
        return matmul(h2,A)
adj=[[0,1,1,0,0,0,0,0],
     [1,0,1,1,0,0,0,0],
     [1,1,0,1,1,0,0,0],
     [0,1,1,0,1,1,0,0],
     [0,0,1,1,0,1,0,1],
     [0,0,0,1,1,0,1,0],
     [0,0,0,0,0,1,0,1],
     [0,0,0,0,1,0,1,0]]
d=int(input())
res=matpow(adj,d)
print(res[0][0])