# 야근 지수

def solution(n, works):
  answer = 0
  works.sort(reverse=True)
  cnt=n
  while cnt:
    if works[0]==0:
      break
    for i in range(len(works)):
      if cnt==0 or works[0]>works[i]:
        break
      works[i]-=1
      cnt-=1
    print(works)
  for i in works:
    answer+=i*i

  return answer


n=1
works=[2, 1, 2]
print(solution(n, works))
