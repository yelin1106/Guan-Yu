# 최솟값 만들기

def solution(A,B):
  answer = 0
  A.sort()
  B.sort(reverse=True)
  for i in range(len(A)):
    answer+=A[i]*B[i]
  return answer

a=[1, 4, 2]
b=[5, 4, 4]
print(solution(a,b))