import io
import sys

_INPUT = """\
6
31 9 24 31 24
0 0 0 0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(len(set(list(map(int,input().split())))))