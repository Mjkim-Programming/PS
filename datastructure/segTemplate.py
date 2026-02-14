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
        self.tree[pos]=val
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