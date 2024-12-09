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
        for i in range(int(ch)):
            pile.append(len(space))
            space.append(int(step))
        step += 1
    else:
        for i in range(int(ch)):
            ls.append(len(space))
            space.append("")
    f = 1 - f

while ls[0] < pile[-1]:
    # print(space)
    idx = ls.pop(0)
    idx2 = pile.pop()
    space[idx] = space[idx2]
    space[idx2] = ''
    ls.append(idx2)
    ls.sort()

ans = 0
print(space)
for i, ch in enumerate(space):
    if ch == '':
        break
    ans += i * ch

print(ans)
