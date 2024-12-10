from collections import defaultdict, deque, Counter
import bisect
from functools import cache
from math import inf
rint = lambda: int(input())
def rlist(n=None):
    if n is None:
        return list(map(int, input().split()))
    return [list(map(int, input().split(''))) for _ in range(n)]
  
n = 8
n = 45

arr = [['' for i in range(n)] for j in range(n)]
zeros = []
for i in range(n):
  x = list(map(int, input()))
  for idx, num in enumerate(x):
    arr[i][idx] = num
    if num == 0:
      zeros.append((i, idx))

dirs = ((0,1), (0, -1), (1,0),(-1,0))

def dfs(i, j, sh):
  if not (0 <= i < n and 0 <= j < n):
    return 0
  
  ans = set()
  
  if arr[i][j] != sh:
    return ans
  
  if arr[i][j] == 9:
    ans.add((i,j))
    return ans
  for di,dj in dirs:
    ni,nj = i+di,j+dj
  
    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == sh + 1:
      ans |= dfs(ni,nj,sh+1)
  return ans

ans = 0
for i,j in zeros:
  # print(dfs(i,j,0))
  ans += len(dfs(i,j,0))
  
print(ans)
