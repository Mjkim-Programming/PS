import sys
input=sys.stdin.readline
stk=[]
line=input().strip()
def prec(op):
    if op in "*/":
        return 2
    if op in "+-":
        return 1
    return 0
res=""
for ch in line:
    if ch.isalpha():
        res+=ch
    elif ch=="(":
        stk.append(ch)
    elif ch==")":
        while stk and stk[-1]!="(":
            res+=stk.pop()
        stk.pop()
    else:
        while stk and prec(stk[-1])>=prec(ch):
            res+=stk.pop()
        stk.append(ch)
while stk:
    res+=stk.pop()
print(res)