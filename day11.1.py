from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split())) for _ in range(n)]
  
arr = rlist()
print(arr)

def find_n(x):
  ans = 0
  for i in x:
    ans = ans * 10 + int(i)
  return ans

for _ in range(25):
  narr = []
  for i in arr:
    if i == 0:
      narr.append(1)
    elif len(str(i)) % 2 == 0:
      xx = str(i)
      x1 = xx[:len(xx) // 2:]
      x2 = xx[len(xx) // 2:]
      narr.append(find_n(x1))
      narr.append(find_n(x2))
    else:
      narr.append(i * 2024)
  arr = narr.copy()
  # print(arr)

print(len(arr))
