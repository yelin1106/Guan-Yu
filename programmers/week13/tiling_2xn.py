# 2xn 타일링

def solution(n):
  tile=[0]*n
  tile[0]=1
  tile[1]=2
  for i in range(2, n):
    tile[i]=(tile[i-1]+tile[i-2])%1000000007
  answer = tile[n-1]
  return answer


print(solution(4))