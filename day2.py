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

def ok(arr, done):
  for i in range(1, len(arr)):
    if not (1 <= arr[i] - arr[i - 1] <= 3):
      if done:
        return 0
      return ok(arr[:i] + arr[i+1:], 1) or ok(arr[:i-1] + arr[i:], 1)
  return 1
      

def f2(arr):
  return ok(arr, 0) or ok(arr[::-1], 0)

def is_monothonic(arr):
  if arr[0] > arr[1]:
    arr = arr[::-1]
  for i in range(len(arr) - 1):
    # if arr[i] >= arr[i + 1]:
    #   return 0
    if not (1 <= arr[i + 1] - arr[i] <= 3):
      return 0
  return 1
ans = ans2 = 0
for i in range(n):
  arr = rlist()
  ans += is_monothonic(arr)
  ans2 += f2(arr)
  
print(ans2)
