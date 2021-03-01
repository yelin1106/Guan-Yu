# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162


def solution(n, computers):
  answer = 0
  check=[False]*n
  for i in range(n):
    if not check[i]:
      queue=[i]
      check[i]=True
      answer+=1
      while queue:
        com=queue.pop(0)
        for j in range(n):
          print(f'com={com}')
          print(computers[com][j])
          if not check[com] and computers[com][j]==1:
            print(f'j={j} {computers[com][j]}')
            queue.append(j)
            check[j]=True
  
  return answer

n=3
computers=[
  [1, 1, 0], 
  [1, 1, 0], 
  [0, 0, 1]]
print(solution(n, computers))