# 주식가격

def solution(prices):
  answer = [0]*len(prices)
  for idx,p in enumerate(prices):
    for i in range(idx+1, len(prices)):
      answer[idx]+=1
      if p>prices[i]:
        break
  return answer


prices=[ 1, 2, 3, 2, 3, 1 ]
print(solution(prices))