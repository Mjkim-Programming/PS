import sys
input=sys.stdin.readline
s=input().rstrip()
stk=[]
for ch in s:
    if ch in "([":
        stk.append(ch)
    else:
        tmp=0
        while stk:
            top=stk.pop()
            if isinstance(top,int):
                tmp+=top
            else:
                if ch==')' and top=='(':
                    stk.append(2 if tmp==0 else 2*tmp)
                    break
                elif ch==']' and top=='[':
                    stk.append(3 if tmp==0 else 3*tmp)
                    break
                else:
                    print(0)
                    sys.exit(0)
        else:
            print(0)
            sys.exit(0)
res=0
for x in stk:
    if isinstance(x,int):
        res+=x
    else:
        print(0)
        sys.exit(0)
print(res)