from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split())) for _ in range(n)]
  
n = 8
n = 45

arr = rlist()
print(arr)

def find_n(x):
  ans = 0
  for i in x:
    ans = ans * 10 + int(i)
  return ans

c = Counter(arr)

for _ in range(75):
  nc = Counter()
  
  for i in c.keys():
    x = c[i]
    if i == 0:
      nc[1] += x
    elif len(str(i)) % 2 == 0:
      xx = str(i)
      x1 = xx[:len(xx) // 2:]
      x2 = xx[len(xx) // 2:]
      x1 = find_n(x1)
      x2 = find_n(x2)
      nc[x1] += x
      nc[x2] += x
    else:
      nc[i * 2024] += x
  c = nc

print(sum(c.values()))
