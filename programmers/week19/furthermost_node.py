# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189
# from collections import deque

# def solution(n, edge):
#   answer=0
#   max_edge=0
#   graph=[[0]*n for _ in range(n)]
#   for x,y in edge:
#     a, b=x-1,y-1
#     graph[a][b]=1
#     graph[b][a]=1
#   check=[0]*n
#   queue=deque()
#   queue.append(0)
#   while queue:
#     node=queue.popleft()
#     for i in range(1,n):
#       if not check[i] and graph[node][i]==1:
#         queue.append(i)
#         check[i]=check[node]+1
#         if check[i]>max_edge:
#           max_edge=check[i]
#           answer=0
#         answer+=1

#   return answer

from collections import deque

def solution(n, edge):
  answer=0
  max_edge=0
  graph=[[] for _ in range(n)]
  for x,y in edge:
    a, b=x-1,y-1
    graph[a].append(b)
    graph[b].append(a)
  check=[0]*n
  queue=deque()
  queue.append(0)
  check[0]=1
  while queue:
    node=queue.popleft()
    for i in graph[node]:
      if not check[i]:
        queue.append(i)
        check[i]=check[node]+1
        if check[i]>max_edge:
          max_edge=check[i]
          answer=0
        answer+=1

  return answer

n=6
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))