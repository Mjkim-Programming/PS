import sys
input=sys.stdin.readline
n=int(input())
if n == 0:
    sys.exit(0)
while n != 0:
    if n==1:
        print(0)
        n=int(input())
        continue
    m,ans,i=n,n,2
    while i*i<=m:
        if m % i == 0:
            ans = ans//i*(i-1)
            while m % i == 0:
                m //= i
        i+=1
    if m>1:
        ans=ans//m*(m-1)
    print(ans)
    n=int(input())