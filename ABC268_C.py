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
  N=int(input())
  p=list(map(int,input().split()))
  ans=[0]*N
  for i in range(N):
    ans[(i-p[i]-1)%N]+=1
    ans[(i-p[i])%N]+=1
    ans[(i-p[i]+1)%N]+=1
  print(max(ans))