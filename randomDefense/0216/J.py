import math
import sys
input=sys.stdin.readline
class Inp:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
a,b,c,d=map(int,input().split())
A,B,C,D=map(int,input().split())
f,s=Inp(a,b,c,d),Inp(A,B,C,D)
def norm(a,b,c,d):
    g=math.gcd(math.gcd(abs(a),abs(b)),abs(c))
    a//=g
    b//=g
    c//=g
    if a<0:
        a=-a
        b=-b
        c=-c
    if c==0:
        d=0
    return a,b,c,d
def add(f,s):
    a=f.a*s.a
    b=f.b*s.a+s.b*f.a
    c=f.c*s.a+s.c*f.a
    d=f.d
    return norm(a,b,c,d)
def sub(f,s):
    a=f.a*s.a
    b=f.b*s.a-s.b*f.a
    c=f.c*s.a-s.c*f.a
    d=f.d
    return norm(a,b,c,d)
def mul(f,s):
    a=f.a*s.a
    b=f.b*s.b+f.c*s.c*f.d
    c=f.b*s.c+s.b*f.c
    d=f.d
    return norm(a,b,c,d)
def div(f,s):
    denom=s.b*s.b-s.c*s.c*s.d
    a=f.a*denom
    b=s.a*(f.b*s.b-f.c*s.c*f.d)
    c=s.a*(f.c*s.b-f.b*s.c)
    d=f.d
    return norm(a,b,c,d)
print(*add(f,s))
print(*sub(f,s))
print(*mul(f,s))
print(*div(f,s))