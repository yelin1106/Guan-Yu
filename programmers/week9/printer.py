# 프린터

def solution(priorities, location):
  answer = 0
  while True:
    temp=priorities.pop(0)
    flag=True #현재 문서를 출력한다
    for p in priorities:
      if p>temp:
        flag=False
        break
    if flag:
      answer+=1
      if location==0:
        break
    else :
      priorities.append(temp)
    location= (location+len(priorities)-1)%len(priorities)
  return answer

priorities=[2, 1, 3, 2]
priorities=[1, 1, 9, 1, 1, 1]
location=2
location=0
print(solution(priorities, location))