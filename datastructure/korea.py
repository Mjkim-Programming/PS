import sys
input=sys.stdin.readline
class SegTree():
    def __init__(self, n):
        self.size=n
        self.tree=[0]*(2*n)
    def build(self, arr):
        for i in range(self.size):
            self.tree[self.size+i]=arr[i]
        for i in range(self.size-1,0,-1):
            self.tree[i]=self.tree[i<<1]+self.tree[i<<1|1]   
    def update(self, pos, val):
        pos+=self.size
        self.tree[pos]+=val
        while pos>1:
            pos>>=1
            self.tree[pos]=self.tree[pos<<1]+self.tree[pos<<1|1]
    def query(self, l, r):
        l+=self.size
        r+=self.size
        res=0
        while l<=r:
            if l&1:
                res+=self.tree[l]
                l+=1
            if not (r&1):
                res+=self.tree[r]
                r-=1
            l>>=1
            r>>=1
        return res
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    tree=SegTree(m+1)
    ans=0
    roads=[tuple(map(int,input().split())) for _ in range(k)]
    roads.sort()
    for a,b in roads:
        if b<m:
            ans+=tree.query(b+1,m)
        tree.update(b,1)
    print(f"Test case {i+1}: {ans}")