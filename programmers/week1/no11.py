#정수 제곱근 판별
#임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
#n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

def solution(n):
  answer = -1
  for i in range(0,n+1):
    if i**2==n:
      answer=(i+1)**2
      break
  return answer


print(solution(1))

#도연&핼 : math의 sqrt사용