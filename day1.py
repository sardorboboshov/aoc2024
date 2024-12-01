from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split())) for _ in range(n)]

n = 1000
a,b = [],[]
aa,bb = Counter(), Counter()
for i in range(n):
    x,y = rlist()
    a.append(x)
    b.append(y)
    aa[x]+=1
    bb[y]+=1
a.sort()
b.sort()
print(sum(abs(i-j) for i,j in zip(a,b)))
s = 0
for i in aa:
    s += i * bb[i]

print(s)