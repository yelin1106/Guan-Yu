# 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(n,answer,x,y):
  if n==1:
    answer.append([x,y])
    return
  hanoi(n-1, answer, x, 6-x-y)
  answer.append([x,y])
  hanoi(n-1, answer, 6-x-y, y)

def solution(n):
  answer = []
  hanoi(n, answer, 1, 3)
  return answer


print(solution(3))