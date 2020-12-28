# 구명보트

#내가 짠 코드 중에 제일 빠른 코드 (효율성 통과 못함)
# def solution(people, limit):
#   answer = 0
#   people.sort(reverse=True)
#   while people:
#     remain=limit-people[0]
#     people.pop(0)
#     for p in people:
#       if p<=remain:
#         people.remove(p)
#         break
#     answer+=1
#   return answer

# 질문하기 참고하고 짠코드 (미쳐벌인 속도)
def solution(people, limit):
  answer = 0
  people.sort(reverse=True)
  idx1=0
  idx2=len(people)-1
  while idx1<=idx2:
    if people[idx1]+people[idx2]<=limit:
      idx2-=1
    idx1+=1
    answer+=1
  return answer

people=[70, 50, 80, 50]
limit=100
print(solution(people,limit))