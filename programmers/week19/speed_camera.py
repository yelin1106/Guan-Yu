# 단속 카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
  answer = 1
  routes.sort(key=lambda x: (x[0], x[1]))
  print(routes)
  min_end=30001
  for start,end in routes[:]:
    print(f'{start} {end} {min_end}')
    if start<=min_end:
      min_end=min(end, min_end)
      continue
    min_end=end
    answer+=1
    print(f'{start} {end} {min_end} {answer}')
  return answer

routes=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]
routes=[[0,2],[2,3],[3,4],[4,6]]
print(solution(routes))