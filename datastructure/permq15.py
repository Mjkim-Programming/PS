import sys
input=sys.stdin.readline
class SegTree():
    def __init__(self, n):
        self.size=n
        self.tree=[(0,0)]*(2*n)
    def build(self, arr):
        for i in range(self.size):
            self.tree[self.size+i]=(arr[i],i)
        for i in range(self.size-1,0,-1):
            self.tree[i]=min(self.tree[i<<1],self.tree[i<<1|1])
    def update(self, pos, val):
        idx=pos
        pos+=self.size
        self.tree[pos]=(val,idx)
        while pos>1:
            pos>>=1
            self.tree[pos]=min(self.tree[pos<<1],self.tree[pos<<1|1])
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
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
tree=SegTree(n)
tree.build(arr)
for _ in range(m):
    q=list(map(int,input().split()))
    if q[0]==2:
        print(tree.tree[1][1]+1)
    else:
        tree.update(q[1]-1,q[2])