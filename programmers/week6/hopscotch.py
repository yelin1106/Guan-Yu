# 땅따먹기

def solution(land):
  answer = 0
  dic={}
  for temp in land:
    print(temp.index(max(temp)))
  return answer

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
