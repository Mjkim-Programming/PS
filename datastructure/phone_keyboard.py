import sys
input=sys.stdin.readline
class Node:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        cur=self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node()
            cur=cur.child[ch]
        cur.end=True
    def search(self,word):
        cur=self.root
        for ch in word:
            if ch not in cur.child:
                return False
            cur=cur.child[ch]
        return cur.end
    def startswith(self,prefix):
        cur=self.root
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur=cur.child[ch]
        return True
    def count_key(self,word):
        cur=self.root
        cnt=0
        for i,ch in enumerate(word):
            if i==0 or cur.end or len(cur.child)>1:
                cnt+=1
            cur=cur.child[ch]
        return cnt
while True:
    line=input().strip()
    if not line:
        break
    n=int(line)
    trie=Trie()
    words=[]
    for _ in range(n):
        w=input().strip()
        words.append(w)
        trie.insert(w)
    total=0
    for w in words:
        total+=trie.count_key(w)
    print(f"{total/n:.2f}")