# 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936
import math

def solution(n, k):
  answer=[]
  check=[False]*(n+1)
  temp=n
  while temp:
    div=math.factorial(temp-1)
    idx=math.ceil(k/div)
    cnt=0
    for i in range(1,n+1):
      if check[i]: continue
      cnt+=1
      if cnt==idx:
        check[i]=True
        answer.append(i)
        break

    k=k%div if k%div else div
    temp-=1
  return answer


print(solution(5,48))