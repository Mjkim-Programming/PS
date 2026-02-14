import sys
input=sys.stdin.readline

import heapq
from collections import deque

n=int(input())
bb,sb,bp,sp={},{},[],[]
orders={}
def clean_buy():
    while bp:
        p=-bp[0]
        q=bb.get(p)
        if not q:
            heapq.heappop(bp)
            continue
        while q and q[0][1]==0:
            q.popleft()
        if q:
            return p
        del bb[p]
        heapq.heappop(bp)
    return 0
def clean_sell():
    while sp:
        p=sp[0]
        q=sb.get(p)
        if not q:
            heapq.heappop(sp)
            continue
        while q and q[0][1]==0:
            q.popleft()
        if q:
            return p
        del sb[p]
        heapq.heappop(sp)
    return 99999
def quote():
    bup=clean_buy()
    aup=clean_sell
    bs=0
    if bup!=0:
        for _,sz in bb[bup]:
            bs+=sz
    asz=0
    if aup!=99999:
        for _,sz in sb[aup]:
            asz+=sz
    print(f"QUOTE {bs} {bp} - {asz} {aup}")
for idx in range(1,n+1):
    parts=input().split()
    trades=[]
    if parts[0]=="BUY":
        q,p=map(int,parts[1:])
        orders[idx]=["BUY",p,q]
        #TODO COMPLETE THIS