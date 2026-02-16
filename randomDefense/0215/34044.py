import sys
input=sys.stdin.readline
n=int(input())
primes=[13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
mods=[v%11 for v in primes]
mmap={}
for i in range(len(primes)):
    mmap[mods[i]]=primes[i]
if n==1:
    print(-1)
    sys.exit(0)
res=""
if n%2==0:
    for _ in range(n//2):
        res+="2343"
else:
    for _ in range((n-3)//2):
        res+="2343"
    res+="232397"
print(res)