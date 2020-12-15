#피보나치 수

# def fibonacci(n):
#   if n==0:
#     return 0
#   if n==1:
#     return 1
#   return fibonacci(n-2)+fibonacci(n-1)

def solution(n):
  answer = 0
  f1=0
  f2=1
  for i in range(2,n+1):
    answer=f1+f2
    f1=f2
    f2=answer
  return answer%1234567


n=5
print(solution(n))