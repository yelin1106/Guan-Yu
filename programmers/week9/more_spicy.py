# 더 맵게

def solution(scoville, k):
  answer = 0
  while min(scoville)<k:
    min1=min(scoville)
    scoville.remove(min1)
    min2=min(scoville)
    scoville.remove(min2)
    scoville.append(min1+min2*2)
    answer+=1
  return answer

scoville=[1, 2, 3, 9, 10, 12]
k=7
print(solution(scoville, k))