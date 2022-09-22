import io
import sys

_INPUT = """\
6
1 1
chokudai
chokudai
2 2
choku
dai
chokudai
choku_dai
2 2
chokudai
atcoder
chokudai_atcoder
atcoder_chokudai
4 4
ab
cd
ef
gh
hoge
fuga
____
_ab_cd_ef_gh_
1 0
ch
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import permutations
  memo={}
  def test(n,k):
    if (n,k) in memo: return memo[(n,k)]
    if n==1: return [[k]]
    res=[]
    for i in range(k+1):
      t=test(n-1,k-i)
      res+=[[i]+t[j] for j in range(len(t))]
    return res

  N,M=map(int,input().split())
  S=[input() for _ in range(N)]
  s=sum([len(S[i]) for i in range(N)])
  T=set([input() for _ in range(M)])
  if N==1:
    if S[0] in T or len(S[0])<3: print(-1)
    else: print(S[0])
  else:
    ans=-1
    b=0
    for k in permutations(range(N)):
      if b==1: break
      for j in range(18-s-N):
        if b==1: break
        tmp=test(N-1,j)
        for l in tmp:
          a=''.join([S[k[i//2]] if i%2==0 else '_'*(l[i//2]+1) for i in range(2*N-1)])
          if a not in T:
            ans=a
            b=1
            break
    print(ans)