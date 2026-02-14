import sys
input=sys.stdin.readline
n=int(input())
if n==1:
    print("Yes")
    print("0 0")
    sys.exit(0)
if (n-1)%4==1 or (n-1)%4==2:
    print("No")
    sys.exit(0)
# Skolem Sequence?
def build(n):
    x=(n+3)//4
    a,b,c,d=2*x-1,4*x-2,4*x-1,4*x
    p,q,r,s=list(range(1,a,2)),list(range(2,a,2)),list(range(a+2,b,2)),list(range(a+1,b,2))
    sp,pp,rp,qp=list(reversed(s)),list(reversed(p)),list(reversed(r)),list(reversed(q))
    if n%4==0:
        return sp+pp+[b]+p+[c]+s+[d]+rp+qp+[b,a]+q+[c]+r+[a,d]
    else:
        return sp+pp+[b]+p+[c]+s+[a]+rp+qp+[b,a]+q+[c]+r
lf=build(n-1)
lf=[0,0]+lf
print("Yes")
print(*lf)