from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split())) for _ in range(n)]


x = input()

space = []
f = 1
step = 0
ls = []
pile = []
for idx, ch in enumerate(x):
    if f:
        pile.append((len(space), int(ch)))
        for i in range(int(ch)):
            space.append(int(step))
        step += 1
    else:
        ls.append((len(space), int(ch)))
        for i in range(int(ch)):
            space.append("")
    f = 1 - f
print(space, ls)
while ls and pile and ls[0][0] < pile[-1][0]:
    # print('sfdffd')
    idx2,nsp = pile.pop()
    ch = space[idx2]
    # print(ch, nsp)
    idx = -1
    sp = -1
    for i, (idxx, spp) in enumerate(ls):
        if idxx > idx2:
            break
        # print(idxx, spp)
        if spp >= nsp:
            idx = idxx
            sp = spp
            break
    # print(ch, nsp, idx)
    if idx == -1:
        continue
    
    ls.pop(i)

    for i in range(nsp):
        space[idx + i] = ch
        space[idx2 + i] = ''
    
    sp -= nsp
    if sp != 0:
        ls.append((idx + nsp, sp))
    ls.sort()
ans = 0
# print(space)
for i, ch in enumerate(space):
    if ch == '':
        continue
    ans += i * ch

print(ans)
        
