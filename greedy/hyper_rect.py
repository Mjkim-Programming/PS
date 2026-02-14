import sys
input=sys.stdin.readline
def calc(arr):
    return arr[0]*arr[1]*arr[2]*arr[3]
idx={"A":0,"B":1,"C":2,"D":3}
ridx={0:"A",1:"B",2:"C",3:"D"}
n,k=map(int,input().split())
cur=list(map(int,input().split()))
cards=[[] for _ in range(4)]
for _ in range(n):
    i,v=input().split()
    cards[idx[i]].append(int(v))
for i in range(4):
    cards[i].sort()
m=calc(cur)
for _ in range(k):
    midx=-10**7
    for i in range(4):
        if not cards[i]:
            continue
        cur[i]+=cards[i][-1]
        tmp=calc(cur)
        cur[i]-=cards[i][-1]
        if tmp>m:
            m,midx=tmp,i
    if midx<0:
        break
    c=cards[midx].pop(-1)
    cur[midx]+=c
    print(ridx[midx],c)