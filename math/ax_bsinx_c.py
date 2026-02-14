from decimal import Decimal, getcontext
import sys
input=sys.stdin.readline
getcontext().prec=60
PI=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
ERROR=Decimal('0.000000000000000000000000000000000000000000001')
def sin(x):
    x=x%(Decimal('2')*PI)
    if x>PI:
        x-=(Decimal('2')*PI)
    term,res,n=x,x,1
    while True:
        term*=-x*x/(Decimal(2*n)*Decimal(2*n+1))
        nres=res+term
        if abs(nres-res)<ERROR:
            break
        if n>=2000:
            break
        res=nres
        n+=1
    return +res
a,b,c=map(int,input().split())
l,r=Decimal('0'),Decimal('2000')
cnt=0
while l<r and (r-l)>ERROR:
    mid=(l+r)/Decimal('2')
    ans=a*mid+b*sin(mid)-c
    if ans>0:
        r=mid
    elif ans<0:
        l=mid
    else:
        break
    cnt+=1
    if cnt>=2000:
        break
print(f"{round(min(l,r),6):.6f}")