from datetime import datetime
import sys
input=sys.stdin.readline
s=input().rstrip()
area=s[:6]
year=s[6:10]
month=s[10:12]
day=s[12:14]
code=s[14:17]
checksum=s[-1]
t=list(map(int,s[:-1].strip()))
n=int(input())
correct=[]
for _ in range(n):
    correct.append(input().rstrip())
if area not in correct:
    print("I")
    sys.exit(0)
try:
    if not (datetime(1900,1,1)<=datetime(int(year),int(month),int(day))<=datetime(2011,12,31,23,59,59,999999)):
        print("I")
        sys.exit(0)
except:
    print("I")
    sys.exit(0)
weights=[pow(2,k,11) for k in range(17,0,-1)]
def check(x,A):
    total=x
    for i in range(17):
        total+=A[i]*weights[i]
    return total%11==1
if checksum=="X":
    checksum="10"
if not check(int(checksum),t):
    print("I")
    sys.exit(0)
if code=="000":
    print("I")
    sys.exit(0)
else:
    if int(code)%2==0:
        print("F")
    else:
        print("M")