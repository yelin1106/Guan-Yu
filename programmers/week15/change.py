# 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907

# 이차원배열 사용 (통과)
def solution(n, money):
  money.sort()
  dp=[[0]*n for _ in range(len(money))]
  for i in range(n):
    dp[0][i]=1 if (i+1)%money[0]==0 else 0
  for i in range(1,len(money)):
    temp=money[i]
    for j in range(n):
      if j<temp-1: # 현재 동전(temp)가 등장하기 전
        dp[i][j]=dp[i-1][j]
      elif j==temp-1: # 현재 동전(temp) 첫 등장
        dp[i][j]=(dp[i-1][j]+1)%1000000007
      else : # 현재 동전(temp) 등장 이후
        dp[i][j]=(dp[i-1][j]+dp[i][j-temp])%1000000007

  answer=dp[-1][n-1]
  return answer

# 일차원 배열 사용 (통과)
# def solution(n, money):
#   money.sort()
#   dp=[0]*n
#   for i in range(n):
#     dp[i]=1 if (i+1)%money[0]==0 else 0
#   for i in range(1,len(money)):
#     temp=money[i]
#     for j in range(n):
#       if j==temp-1:
#         dp[j]=(dp[j]+1)%1000000007
#       elif j>temp-1:
#         dp[j]=(dp[j]+dp[j-temp])%1000000007
#   answer=dp[n-1]
#   return answer

n=5
money=[1,2,5]
print(solution(n, money))