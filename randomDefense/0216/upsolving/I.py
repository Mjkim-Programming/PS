import sys
input=sys.stdin.readline
n=int(input())
INF=10**9
dp=[INF]*(n+1)
prev={"B":"J","O":"B","J":"O"}
