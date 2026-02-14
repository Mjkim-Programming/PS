import math
import sys
input=sys.stdin.readline
A,B,C,D=map(int,input().split())
if A==0:
    if D!=0 and B==0 and C==0:
        print(0)
    if D!=0 and B!=0 and C!=0:
        #TODO 베주 항등식 판별 구현
        pass
    else:
        print("INFINITY")
    sys.exit(0)
#TODO A!=0일 때 구현