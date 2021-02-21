# 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938


def solution(n, s):
  if n>s:
    return [-1]
  div, remain=divmod(s,n)
  answer=[div]*n
  for i in range(1,remain+1):
    answer[-i]+=1
  return answer

print(solution(2,9))