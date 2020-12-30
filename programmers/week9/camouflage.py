# 위장

def solution(clothes):
  answer = 1
  dic={}
  for c,t in clothes:
    if t in dic.keys():
      dic[t]=dic[t]+1
    else:
      dic[t]=1
  print(dic)
  for v in dic.values():
    answer*=(v+1)
  answer-=1
  return answer


clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))