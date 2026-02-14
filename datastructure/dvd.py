import sys
input=sys.stdin.readline
INF=float('INF')
class SegTree():
    def __init__(self, n):
        self.size=n
        self.tree=[(INF,-INF)]*(2*n)
    def build(self, arr):
        for i in range(self.size):
            self.tree[self.size+i]=arr[i]
        for i in range(self.size-1,0,-1):
            self.tree[i]=(min(self.tree[i<<1][0],self.tree[i<<1|1][0]),max(self.tree[i<<1][1],self.tree[i<<1|1][1]))
    def update(self, pos, val):
        pos+=self.size
        self.tree[pos]=val
        while pos>1:
            pos>>=1
            self.tree[pos]=(min(self.tree[pos<<1][0],self.tree[pos<<1|1][0]),max(self.tree[pos<<1][1],self.tree[pos<<1|1][1]))
    def query(self, l, r):
        l+=self.size
        r+=self.size
        mn,mx=INF,-INF
        while l<=r:
            if l&1:
                mn,mx=min(mn,self.tree[l][0]),max(mx,self.tree[l][1])
                l+=1
            if not (r&1):
                mn,mx=min(mn,self.tree[r][0]),max(mx,self.tree[r][1])
                r-=1
            l>>=1
            r>>=1
        return mn,mx
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    tree=SegTree(n)
    tree.build([(i,i) for i in range(n)])
    for _ in range(k):
        q,a,b=map(int,input().split())
        if q==0:
            va,vb=tree.query(a,a),tree.query(b,b)
            tree.update(a,vb)
            tree.update(b,va)
        elif q==1:
            mn,mx=tree.query(a,b)
            print("YES" if mn==a and mx==b else "NO")