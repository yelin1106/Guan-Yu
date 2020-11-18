#최대공약수와 최소공배수
#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


def solution(n, m):
  divNum=2
  gcd=1 #최대공약수
  lcm=1 #최소공배수
  x=n
  y=m
  while divNum<=min(x,y):
    if (x%divNum==0) and (y%divNum==0):
      x/=divNum
      y/=divNum
      gcd*=divNum
    else:
      divNum+=1
  divNum=2
  x=n
  y=m
  while divNum<=max(x,y):
    if (x%divNum==0) or (y%divNum==0):
      if x%divNum==0:
        x/=divNum
      if y%divNum==0:
        y/=divNum
      lcm*=divNum
    else:
      divNum+=1
  answer = [gcd, lcm]
  return answer

print(solution(3,12))

#도연이거 훔치기
#해린언니거 : 두 수 곱=최대*최소, 큰 수를 작은수로 나누고, 큰 수를 그 몫으로 바꾸고, 작은 수를 그 나머지로 바꾼 후 나머지가 0이 될 때 까지 반복