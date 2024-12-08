from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split())) for _ in range(n)]


n = 12
n = 50
arr = [["" for i in range(n)] for j in range(n)]
d = defaultdict(list)
seen = set()
for i in range(n):
    x = input()
    for idx,ch in enumerate(x):
        arr[i][idx] = ch
        if ch != '.':
            d[ch].append((i, idx))

def do(seen, ls, i, j, arr):
    y1, x1 = ls[i]
    y2, x2 = ls[j]
    dy = y2 - y1
    dx = x2 - x1

    ny,nx = y1, x1
    while 0 <= ny < n and 0 <= nx < n:
        arr[ny][nx] = '#'
        seen.add((ny, nx))
        ny -= dy
        nx -= dx

    ny,nx = y2, x2
    while 0 <= ny < n and 0 <= nx < n:
        seen.add((ny, nx))  
        arr[ny][nx] = '#' 
        ny += dy
        nx += dx

for v in d.values():
    k = len(v)
    if k == 1:
        continue
    for i in range(k):
        for j in range(i + 1, k):
            do(seen, v, i, j, arr)
# print(arr)
print(len(seen))
# for row in arr:
#     print(" ".join(f"{item:>5}" for item in row))
