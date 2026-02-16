import sys
input=sys.stdin.readline
while True:
    s=input().strip()
    if s=="00e0":
        break
    n,m=map(int,s.split("e"))
    num=n*(10**m)
    hig=1<<(num.bit_length()-1)
    print((num-hig)*2+1)