import io
import sys

_INPUT = """\
6
4
1 2 0 3
3
0 1 2
10
3 9 6 1 7 2 8 0 5 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  N=int(input())
  p=list(map(int,input().split()))
  d={p[i]:i for i in range(N)}
  K=[0]*N
  if N%2==1:
    for i in range(N):
      K[(i-d[i])%N]+=2
      K[(i+N//2-d[i])%N]-=1
      K[(i+N//2-d[i]+1)%N]-=1
  else:
    for i in range(N):
      K[(i-d[i])%N]+=2
      K[(i+N//2-d[i])%N]-=2
  K[0]=sum([min((i-d[i]-1)%N,(d[i]+1-i)%N) for i in range(N)])-sum([min((i-d[i])%N,(d[i]-i)%N) for i in range(N)])
  K=list(accumulate(K))
  K=list(accumulate(K))
  print(min(K)+sum([min((i-d[i])%N,(d[i]-i)%N) for i in range(N)]))