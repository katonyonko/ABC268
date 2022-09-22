import io
import sys

_INPUT = """\
6
atco
atcoder
code
atcoder
abc
abc
aaaa
aa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=input()
  if len(S)<=len(T) and S==T[:len(S)]: print('Yes')
  else: print('No')