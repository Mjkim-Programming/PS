import sys
input=sys.stdin.readline
# Basic Class
MOD=10000
SIZE=27
class Matrix:
    def __init__(self,mat=None):
        if mat:
            self.m=mat
        else:
            self.m=[[0]*SIZE for _ in range(SIZE)]
    @staticmethod
    def identity():
        m=Matrix()
        for i in range(SIZE):
            m.m[i][i]=1
        return m
    def __matmul__(self,other):
        res=Matrix()
        for i in range(SIZE):
            for k in range(SIZE):
                if self.m[i][k]==0:
                    continue
                for j in range(SIZE):
                    res.m[i][j]=(res.m[i][j]+self.m[i][k]*other.m[k][j])%MOD
        return res
    def pow(self,n):
        res=Matrix.identity()
        base=self
        while n:
            if n&1:
                res=res@base
            base=base@base
            n>>=1
        return res
class Node:
    def __init__(self,typ):
        self.typ=typ
        self.children=[]
        self.repeat_count=0
        self.matrix=None
        self.has_print=False
        self.var=None
    def eval(self):
        if self.typ=="assign":
            return self.matrix, False
        if self.typ=="print":
            return Matrix.identity(), True
        if self.typ=="sequence":
            current=Matrix.identity()
            has_print=False
            for child in self.children:
                m,hp=child.eval()
                current=m @ current
                has_print |= hp
            return current, has_print
        if self.typ=="repeat":
            m,hp=self.children[0].eval()
            if not hp:
                return m.pow(self.repeat_count), False
            else:
                return None, True
# Process Program Input
program_stk=[]
while True:
    line=input()
    if not line.strip():
        break
    program_stk.append(line.lstrip().rstrip())
print(program_stk)