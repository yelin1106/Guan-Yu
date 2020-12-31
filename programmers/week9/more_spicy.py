# 더 맵게

#효율성 X
# def solution(scoville, k):
#   answer = 0
#   while min(scoville)<k:
#     if len(scoville)<2: break
#     scoville.sort()
#     min1=scoville[0]
#     scoville.pop(0)
#     min2=scoville[0]
#     scoville.pop(0)
#     scoville.append(min1+min2*2)
#     answer+=1
#   if min(scoville)<k:
#     answer=-1
#   return answer

import heapq

def solution(scoville, k):
  answer = 0
  scoville.sort()
  while scoville[0]<k:
    if len(scoville)<2: break
    min1=heapq.heappop(scoville)
    min2=heapq.heappop(scoville)
    heapq.heappush(scoville, min1+min2*2)
    answer+=1
  if scoville[0]<k:
    answer=-1
  return answer

scoville=[1, 2, 3, 9, 10, 12]
k=7
print(solution(scoville, k))