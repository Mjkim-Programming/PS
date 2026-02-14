import math
import sys
input=sys.stdin.readline

g = 9.81

T = int(input())
for _ in range(T):
    j, p, H, L = map(int, input().split())
    x, y = 0, 0
    v0 = math.sqrt(2*g*j)
    
    def h_func(l):
        if l < 0:
            return H
        if l < L/2:
            return H*(1-2*(l/L)*(l/L))
        if l < L:
            return 2*H*(l/L - 1)*(l/L - 1)
        return 0
    
    def f_func(l):
        return -l*l/(4*j) + H + p
    
    def find_intersection(l, h , eps=1e-9):
        while h - l > eps:
            mid = (l + h) / 2
            if h_func(mid) < f_func(mid):
                l = mid
            else:
                h = mid
        return (l + h) / 2
    
    x = find_intersection(0, 1e9)
    y = f_func(x)
    
    def v():
        return math.sqrt(2*g*(j+p+H-y))
    
    def h_prime(l):
        if l < 0:
            return 0
        if l < L/2:
            return -4*H*l/(L*L)
        if l < L:
            return (4*H)*(l/L - 1)/L
        return 0
    
    def f_prime(l):
        return -l/(2*j)
    
    def alp(l):
        fp = f_prime(l)
        hp = h_prime(l)
        res = math.atan(math.fabs((hp-fp)/(1+fp*hp)))
        return (180 * res) / math.pi
    
    print(f"{x:.10f} {v():.10f} {alp(x):.10f}")