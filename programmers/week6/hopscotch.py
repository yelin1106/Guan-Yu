# 땅따먹기

def solution(land):
  answer = 0
  for idx, l in enumerate(land):
    if idx==0: continue
    for i in range(len(l)):
      l[i]+=max(land[idx-1][:i]+land[idx-1][i+1:])
  answer=max(land[-1])
  return answer

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
