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
5
d
a
dcfg
axc
dcfb
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mode=0
  import sys
  sys.setrecursionlimit(10**6)
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

  memo={}
  def rec(i):
    if i in memo: return memo[i]
    tmp=0
    for v in G[i]:
      if v!=parent[i]: tmp+=rec(v)+1
    memo[i]=tmp
    return memo[i]

  mod=998244353
  N=int(input())
  S=[""]+[input() for _ in range(N)]
  T=sorted([(S[i],i) for i in range(N+1)])
  if mode==1: print(T)
  G=[[] for _ in range(N+1)]
  parent=[-1]*(N+1)
  now=0
  for i in range(1,N+1):
    s,id=T[i]
    l=0
    if mode==1:
      if s=='dcfb': print(T[now][0],l)
    for j in range(min(len(S[now]),len(s))):
      if S[now][j]==s[j]: l+=1
      else: break
    while len(S[now])>l: now=parent[now]
    G[now].append(id)
    G[id].append(now)
    parent[id]=now
    now=id
  D=bfs(G,0)
  den=pow(2,mod-2,mod)
  if mode==1: print(G)
  for i in range(N):
    if mode==1: print((N+D[i+1]-rec(i+1))*den%mod,D[i+1]-1,rec(i+1))
    else: print((N+D[i+1]-rec(i+1))*den%mod)