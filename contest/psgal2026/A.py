import sys
input=sys.stdin.readline
n=int(input())
s=input().rstrip()
target="eagle"
mc=5
for i in range(n-4):
    cc=0
    for j in range(5):
        if s[i+j]!=target[j]:
            cc+=1
    mc=min(mc,cc)
print(mc)