from functools import cmp_to_key
import io
import sys

_INPUT = """\
6
3
1X3
59
XXX
10
X63X395XX
X2XX3X22X
13
3716XXX6
45X
X6XX
9238
281X92
1XX4X4XX6
54X9X711X1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from functools import cmp_to_key
  def cmp(a, b):
    if a == b: return 0
    return -1 if a[1]*b[0] < b[1]*a[0] else 1

  N=int(input())
  S=[input() for _ in range(N)]
  J=[(S[i].count('X'),sum([int(S[i][j]) for j in range(len(S[i])) if S[i][j]!='X']),i) for i in range(N)]
  J=sorted(J,key=cmp_to_key(cmp))
  ans=0
  x=0
  t=''.join([S[J[i][2]] for i in range(N)])
  for i in range(len(t)):
    if t[i]=='X': x+=1
    else: ans+=x*int(t[i])
  print(ans)