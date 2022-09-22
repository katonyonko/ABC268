import io
import sys

_INPUT = """\
6
3
a
aa
ab
3
a
aa
aaa
2
abef
abe
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  mod=998244353
  N=int(input())
  memo=[0]*(N+1)
  def rec(G,s):
    if memo[s]!=0: return memo[s]
    res=1
    for v in G[s]:
      if depth[v]>depth[s]: res+=rec(G,v)
    memo[s]=res
    return res
  S=[input() for _ in range(N)]
  d={S[i]:i+1 for i in range(N)}
  d['']=0
  G=[[] for _ in range(N+1)]
  SS=sorted(S,key=lambda x:len(x))
  used=set([''])
  for i in range(N):
    tmp=len(SS[i])
    while SS[i][:tmp] not in used:
      tmp-=1
    used.add(SS[i])
    G[d[SS[i]]].append(d[SS[i][:tmp]])
    G[d[SS[i][:tmp]]].append(d[SS[i]])
  depth=bfs(G,0)
  rec(G,0)
  x=pow(2,mod-2,mod)
  for i in range(N):
    a,b=depth[d[S[i]]],memo[d[S[i]]]-1
    print((N+a-b)*x%mod)