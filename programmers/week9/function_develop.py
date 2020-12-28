# 기능개발

def solution(progresses, speeds):
  answer = []
  while progresses:
    for i in range(len(progresses)):
      progresses[i]+=speeds[i]
    if progresses and progresses[0]>=100:
      ans=0
      while progresses and progresses[0]>=100:
        progresses.pop(0)
        speeds.pop(0)
        ans+=1
      answer.append(ans)
  return answer


progresses=[95, 95, 95, 95] # 2 2 3 5
speeds=[4, 3, 2, 1] #[2,1,1]
print(solution(progresses, speeds))