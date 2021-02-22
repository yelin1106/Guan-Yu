# N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

def bt(n, depth, arr1, arr2, arr3):
  ans=0
  if n==depth:
    return 1
  for i in range(n):
    if not (arr1[i] or arr2[depth+i] or arr3[depth-i+n-1]):
      arr1[i]=arr2[depth+i]=arr3[depth-i+n-1]=True
      ans+=bt(n, depth+1, arr1, arr2, arr3)
      arr1[i]=arr2[depth+i]=arr3[depth-i+n-1]=False
  return ans

def solution(n):
  arr1=[False]*n #가로, 세로
  arr2=[False]*(n*2-1) #우상향 대각선 (x+y)
  arr3=[False]*(n*2-1) #좌상향 대각선 (x-y+n-1)
  answer=bt(n, 0, arr1, arr2, arr3)

  return answer


print(solution(4))