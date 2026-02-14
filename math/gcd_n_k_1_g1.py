import sys
input=sys.stdin.readline
n=int(input())
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